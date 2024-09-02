FROM python:3.10-alpine
WORKDIR /home/sardor/bg_data/exec_3/src
RUN apk add gcc
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["/bin/sh"]
