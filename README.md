# Finance_RAG

## Запуск (команда sega)

##### Склонируйте репозиторий

```
git clone https://github.com/Yagorka/Finance_RAG.git sega_rag
cd sega_rag
```
##### Добавьте файл config.py в директорию src
```
api_key = "..."
folder_id = ".."
```

##### Соберите образ и запустите образ
```
sudo docker build . -t sega_rag
sudo docker run -it sega_rag sh
```
чат бот развернутна порту: http://127.0.0.1:7860
