FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive 

COPY . /BooksApp

RUN apt update

RUN apt-get update -y 
RUN apt-get install python3-pip  -y
WORKDIR /BooksApp
RUN pip3 install -r requirements.txt
RUN export PYTHONPATH=$PYTHONPATH:/BooksApp
ENV PYTHONPATH /BooksApp

CMD ["python3", "/BooksApp/server/app.py"]