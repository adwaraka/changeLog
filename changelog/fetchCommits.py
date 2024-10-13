import argparse
import requests
import datetime
import heapq
import nltk
import re
import os
import time

from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


def extractCommits(user: str, repo: str):
    try:
        headers = {'Authorization': 'token ' + os.environ.get('GIT_ACCESS_TOKEN')}
        gitURL = f'https://api.github.com/repos/{user}/{repo}/commits'
        response = requests.get(gitURL, headers=headers, verify=False)
        # ?since=2024-01-01T00:00:00Z append to url for commits
        # abs(
        #     (datetime.now() - datetime.strptime(date.split("T")[0], "%Y-%m-%d")
        #         ).days) gives difference in days

        summaryText = ""
        # print()
        # print(f"CHANGE LOG DATE:{datetime.datetime.now().isoformat()}")
        # print()
        for val in response.json():
            # print(f"Commit Date:{val['commit']['author']['date']}")
            # print("\t", val['commit']['message'])
            summaryText+=val['commit']['message']
            summaryText+=". "
            # print()
    except Exception as err:
        raise Exception("Cannot fetch commits from the username/repo. {}".format(err))

    try:
        # print(f"All Commits:\n {summaryText}")
        calculateSummary(summaryText, user, repo)
    except Exception as err:
        raise Exception("Something went wrong with summarizing. {}".format(err))


def calculateSummary(summaryText: str, user: str, repo: str):
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    sentences = nltk.sent_tokenize(summaryText)
    stopwords = nltk.corpus.stopwords.words('english')

    # Removing Square Brackets and Extra Spaces
    summaryText = re.sub(r'\[[0-9]*\]', ' ', summaryText)
    summaryText = re.sub(r'\s+', ' ', summaryText)

    # Removing special characters and digits
    formattedSummaryText = re.sub('[^a-zA-Z]', ' ', summaryText )
    formattedSummaryText = re.sub(r'\s+', ' ', formattedSummaryText)

    wordFrequencies = {}
    for word in nltk.word_tokenize(formattedSummaryText):
        if word not in stopwords:
            if word not in wordFrequencies.keys():
                wordFrequencies[word] = 1
            else:
                wordFrequencies[word] += 1

    maxFrequency = max(wordFrequencies.values())

    for word in wordFrequencies.keys():
        wordFrequencies[word] = (wordFrequencies[word]/maxFrequency)

    sentenceScores = {}
    for sent in sentences:
        for word in nltk.word_tokenize(sent.lower()):
            if word in wordFrequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentenceScores.keys():
                        sentenceScores[sent] = wordFrequencies[word]
                    else:
                        sentenceScores[sent] += wordFrequencies[word]

    summarySentences = heapq.nlargest(10, sentenceScores, key=sentenceScores.get)
    changeClassifier(summarySentences, user, repo)


def changeClassifier(sentences: list, user: str, repo: str):
    classifier = {'add':       [],
                  'change':    [],
                  'remove':    [],
                  'deprecate': [],
                  'fix':       [],
                  'security':  [],
                  }
    misc = []
    isClassifed = False

    for sentence in sentences:
        for classifyTerm in classifier.keys():
            if classifyTerm in sentence.lower():
                classifier[classifyTerm].append(f'{sentence}')
                isClassifed = True
                break
        if not isClassifed:
            misc.append(f'{sentence}\n')
        isClassifed = False

    ts = time.time()
    currentTimeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')

    try:
        #create directory and then the file in it
        directory = f'./data/{user}/{repo}/'
        filePath = f'{directory}' + f'change_log_{currentTimeStamp}.txt'
        os.makedirs(directory, exist_ok=True)

        with open(filePath, 'w') as fp:
            for key, value in classifier.items():
                fp.write(f'\n\n### {key} ###\n')
                for comment in value:
                    fp.write(f' - {comment}\n')
            fp.write(f'\n\n### others ###\n')
            for comment in misc:
                fp.write(f' - {comment}')
            print(f"File /data/change_log_{currentTimeStamp}.txt generated.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", help="user")
    parser.add_argument("--repo", help="repo")
    args = parser.parse_args()
    extractCommits(args.user, args.repo)


if __name__ == "__main__":
    main()