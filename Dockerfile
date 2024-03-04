FROM python:3.7.13-alpine
WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8080

CMD ["python", "./server.py"]