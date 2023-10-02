FROM python:3
WORKDIR /app-flask
ARG PORT_BUILD=5000
ARG PORT_MONGO=27017
ARG HOST_MONGO=localhost
ENV port_mongo=PORT_MONGO
ENV host_mongo=HOST_MONGO
ENV port=PORT_BUILD
EXPOSE $PORT_BUILD
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python3 NoticiasFlaskinhas.py