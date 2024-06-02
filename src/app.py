import gradio as gr
import random
import time
import pickle
import os

from yandex_chain import YandexLLM, YandexEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

from config import api_key, folder_id

embeddings = YandexEmbeddings(folder_id=folder_id, api_key=api_key)
new_db = FAISS.load_local(os.path.join('./data', 'faiss_index'), embeddings,allow_dangerous_deserialization=True)

with open(os.path.join('./data', 'saved_dictionary_name.pkl'), 'rb') as f:
    loaded_dict = pickle.load(f)

last_company = ''
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    button = gr.Button("Отправить")
    clear = gr.ClearButton([msg, chatbot])
    def respond(input, history=None):
        company = []
        for k, v in loaded_dict.items():
            for i in v:
                if i in input.lower():
                    company.append(i)
        last_company_one =f'{company[0]}' if len(company) >0 else last_company
        dop_text =f'смотри отчет {(", ".join[loaded_dict[last_company_one]][:2])}' if len(company) >0 else last_company_one  
        retriever = new_db.as_retriever(search_type="similarity", 
                                    search_kwargs={'k':2, 'fetch_k':6, 'filter':None})#lambda d: 'РСХБ' in d["source"]
        
        query = dop_text + input #"Как называется компания описанная в документе?"

        print(f"+ Query: {query}")

        print(" + Getting relevant documents")
        # res = retriever.get_relevant_documents(query)

        template = """Представь что ты квалифицированный финансовый аналитик. Анализируя отчет ответь на вопрос ориентируясь только на контекст:
        {context}

        Вопрос: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        model = YandexLLM(folder_id=folder_id, api_key=api_key)

        chain = (
            {"context": retriever, "question": RunnablePassthrough()} 
            | prompt 
            | model 
            | StrOutputParser()
        )

        print(" + Running LLM Chain")

        res = chain.invoke(query)

        print(f" + Ответ: {res}")
        if history is None:
            history = []
        print(res)
        history.append((input, res))
        return '', history

    # def respond(message, chat_history):
    #     bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    #     chat_history.append((message, bot_message))
    #     return "", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    button.click(respond, [msg, chatbot], [msg, chatbot])
demo.launch(share=True)