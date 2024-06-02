FROM python:3.10-slim
WORKDIR /app

COPY . /app

VOLUME /app/data

RUN pip3 install -r requirements.txt

CMD ["python3","src/app.py"]
