# syntax=docker/dockerfile:1
FROM python:3.9-bullseye
WORKDIR /run
COPY dependencies.txt dependencies.txt
RUN pip install -r dependencies.txt
COPY src .
CMD python main.py