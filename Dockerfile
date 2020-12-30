FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=flask_server.py

CMD flask run --host=0.0.0.0
