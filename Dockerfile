FROM python:3.10.0-alpine

RUN pip install requests nltk

WORKDIR /code
COPY ./data /code/data
COPY . .

ENTRYPOINT ["python", "fetchCommits.py"]