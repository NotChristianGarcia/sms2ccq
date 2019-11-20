FROM python:3.7-alpine

COPY libs/ccqclient/ccqclient ./twilio/ccqclient
COPY ccq_api.py twilio_server.py messaging.py  ./twilio/

RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip3 install flask redis webdavclient3

CMD ["python3", "./twilio/twilio_server.py"]