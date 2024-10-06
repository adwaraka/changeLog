FROM python:3.10.0-alpine

RUN pip install requests nltk

WORKDIR /code
ADD fetchCommits.py .
ENTRYPOINT ["python", "fetchCommits.py"]