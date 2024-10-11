FROM python:3.10.0-alpine

WORKDIR /code
COPY . .

RUN pip install requests
EXPOSE 8000
CMD ["python3", "server.py"]