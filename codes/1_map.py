#!/usr/bin/python3
"""mapper.py"""

import sys

# Loop over each line from the standard input
for line in sys.stdin:
    line = line.strip()
    document = line.split()

    # Skip the line if it contains less than 3 words (ID + at least one bigram)
    if len(document) < 3:
        continue
    document_id = document[0]
    for i in range(1, len(document) - 1):
        print(f"{document[i]} {document[i+1]} {document_id}")
