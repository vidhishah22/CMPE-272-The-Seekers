FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt \
 && apt-get update \
 && apt-get install -y vim
ADD . /code/

#FROM ubuntu:latest
#RUN apt-get update \
#  && apt-get install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 install --upgrade pip \
#  && mkdir /code
#
#WORKDIR /code
#ADD requirements.txt /code/
#RUN cd /code \
# && pip install -r requirements.txt
#ADD . /code/
#RUN pwd \
# && ls -alrth