FROM nginx:alpine

RUN apk update && apk upgrade

WORKDIR /app

COPY . .

COPY ./web/nginx.conf /etc/nginx/nginx.conf 