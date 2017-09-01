FROM python:2


ADD main.py /

ENV CONFIG config.ini
ADD config.ini $CONFIG

RUN pip install \
	configparser \
	pymongo \
	slackclient

VOLUME /data/db

CMD [ "python", "./main.py"]
#CMD ["sleep", "180"]

