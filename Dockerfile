#FROM gcr.io/google_appengine/python:latest
FROM python:3.9

#change to this working directory of 'app'
WORKDIR /app

ADD . /app

#copy requirements to "app"
COPY ./requirements.txt /app

#copy protos to "app"
COPY ./protos /app

#copy datas.json to 'app'
COPY ./datas /app

#copy location.json to 'app'
#COPY ./datas/location.json /app

#copy script to 'app'
COPY ./safeentry_server.py /app
COPY ./safeentry_db.py /app
COPY ./safeentry_pb2.py /app
COPY ./safeentry_pb2_grpc.py /app
COPY ./safeentry_client.py /app

RUN pip install --upgrade pip

#Install python Dependecies
RUN pip install --no-cache-dir -r requirements.txt --no-dependencies

ENTRYPOINT ["python", "-u", "safeentry_server.py"]

