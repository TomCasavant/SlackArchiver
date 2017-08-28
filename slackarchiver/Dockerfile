FROM python:2

ADD main.py /


RUN pip install \
	configparser \
	pymongo \
	slackclient

CMD [ "python", "/main.py"]


