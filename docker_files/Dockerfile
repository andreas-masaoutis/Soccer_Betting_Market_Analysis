FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/andreas-masaoutis/Soccer_Betting_Market_Analysis
    && git checkout dev

WORKDIR /Soccer_Betting_Market_Analysis
 
RUN cd project_documents \
    && pip install -r requirements.txt

EXPOSE 8050

CMD python index.py
