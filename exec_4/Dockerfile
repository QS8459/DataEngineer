FROM python:3.10-alpine
WORKDIR /home/sardor/bg_data/exec_4/src
RUN apk add --no-cache \
    gcc \
    python3-dev
EXPOSE 80
COPY src/requirements.txt requirement.txt
RUN pip install -r requirement.txt
CMD ["/bin/sh"]    
