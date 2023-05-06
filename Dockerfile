FROM python:3.8-slim-buster

WORKDIR /Soccer_Betting_Market_Analysis

COPY . .

RUN apt-get -y update \
    && cd project_documents \
    && pip install -r requirements.txt \
    && pip cache purge

EXPOSE 8050

WORKDIR app_files

CMD python index.py
