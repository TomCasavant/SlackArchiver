FROM python:2


ADD main.py slackarchiver

ENV CONFIG config.ini
ADD config.ini $CONFIG

RUN pip install \
	configparser \
	pymongo \
	slackclient


CMD [ "python", "\slackarchiver\main.py"]
#sleep 18000

