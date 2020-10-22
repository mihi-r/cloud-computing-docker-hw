FROM python:3.7-alpine3.12

WORKDIR /

COPY main.py .

RUN mkdir -p /home/data

RUN mkdir -p /home/output

CMD python3 main.py