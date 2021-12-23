from python:3.9.0a3-alpine3.10

LABEL MAINTAINER="Sandeep Rathor <sandeeprathor509@gmail.com>"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["behave"]