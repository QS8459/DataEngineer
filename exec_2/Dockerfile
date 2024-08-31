FROM python:3.10-alpine
WORKDIR /src
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    python3-dev \
    py3-pip \
    build-base \
    && pip install --upgrade pip
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall -y scipy scikit-learn
RUN pip install --use-feature=no-binary-enable-wheel-cache scipy scikit-learn
COPY /src /src
CMD ["python3","-m","main", "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"]
