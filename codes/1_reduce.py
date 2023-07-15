#!/usr/bin/python3
"""reducer.py"""

import sys

def process_bigram(last_bigram, documents_occurence):
    if last_bigram:
        occurences = [f"{doc}:{count}" for doc, count in documents_occurence.items()]
        print(f"{last_bigram} {' '.join(occurences)}")

last_bigram = None
documents_occurence = {}

for line in sys.stdin:
    line = line.strip()
    bigram, doc_id = line.rsplit(' ', 1)

    if bigram != last_bigram:
        process_bigram(last_bigram, documents_occurence)
        last_bigram = bigram
        documents_occurence = {}

    documents_occurence[doc_id] = documents_occurence.get(doc_id, 0) + 1

process_bigram(last_bigram, documents_occurence)
