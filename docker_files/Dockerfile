FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/andreas-masaoutis/Soccer_Betting_Market_Analysis

WORKDIR /Soccer_Betting_Market_Analysis
 
RUN git checkout dev \
    && cd project_documents \
    && pip install -r requirements.txt \
    && pip cache purge
    
EXPOSE 8050

CMD python index.py
