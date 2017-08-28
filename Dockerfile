FROM python:2

ADD main.py /


RUN pip install configparser

RUN pip install pymongo

RUN pip install slackclient

CMD [ "python", "./main.py"]


