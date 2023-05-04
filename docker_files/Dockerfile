FROM python:3.8-alpine

RUN apk update \
    && apk add git \
    && git clone https://github.com/andreas-masaoutis/Soccer_Betting_Market_Analysis

WORKDIR /Soccer_Betting_Market_Analysis
 
RUN git checkout dev \
    && cd project_documents \
    && pip install -r requirements.txt

EXPOSE 8050

CMD python index.py
