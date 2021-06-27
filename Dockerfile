#syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .

ENV DISPLAY :0

CMD ["python3","main.py"]



