FROM python:2


ADD main.py /

ENV CONFIG config.ini
ADD config.ini $CONFIG

RUN pip install \
	configparser \
	pymongo \
	slackclient


CMD [ "python", "./main.py"]
#CMD ["sleep", "1800"]

