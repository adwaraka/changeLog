import requests
import datetime
import heapq
import nltk
import re
import os
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

headers = {'Authorization': 'token ' + os.environ.get('GIT_ACCESS_TOKEN')}
login = requests.get(
	'https://api.github.com/repos/adwaraka/neighbors/commits', 
	headers=headers, 
	verify=False)
# ?since=2024-01-01T00:00:00Z append to url for commits
# abs((datetime.now() - datetime.strptime(date.split("T")[0], "%Y-%m-%d")).days) gives difference in days


summaryText = ""

# print()
# print(f"CHANGE LOG DATE:{datetime.datetime.now().isoformat()}")
# print()
for val in login.json():
	# print(f"Commit Date:{val['commit']['author']['date']}")
	# print("\t", val['commit']['message'])
	summaryText+=val['commit']['message']
	summaryText+=". "
	# print()

# print(f"All Commits:\n {summaryText}")


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

summary = '\n-'.join(summarySentences)
print(f"Summary:\n{summary}")
