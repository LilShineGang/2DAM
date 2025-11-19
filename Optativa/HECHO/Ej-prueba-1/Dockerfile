FROM alpine

RUN apk update && apk add python3

WORKDIR /app

COPY . /app

CMD ["python3", "main.py"]