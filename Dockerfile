FROM python:3.7-alpine

RUN apk --no-cache add build-base gcc

WORKDIR /src

#ADD https://github.com/micropython/micropython/releases/download/v1.11/micropython-1.11.tar.gz ./
#RUN tar -xzf micropython-1.11.tar.gz && ln -s micropython-1.11 micropython
# mpy-cross
#RUN cd micropython/mpy-cross && make

COPY src /src

RUN rm -rf build/*
