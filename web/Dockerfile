FROM nginx:alpine

RUN apk update && apk upgrade

WORKDIR /app

COPY . .

COPY ./nginx.conf /etc/nginx/nginx.conf 