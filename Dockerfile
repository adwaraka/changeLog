FROM python:3.10.0-alpine

WORKDIR /code
ADD fetchCommits.py .

RUN pip install requests nltk
ENTRYPOINT ["python", "fetchCommits.py"]