import math
import re
from collections import Counter
import os
import glob

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

count = 0
path = '/home/vini/Downloads/MR/codesOfConduct'
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        arq1line = f.read()
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with open(os.path.join(os.getcwd(), filename), 'r') as e:
                arq2line = e.read()
                vector1 = text_to_vector(arq1line)
                vector2 = text_to_vector(arq2line)
                count = count + 1
                cosine = get_cosine(vector1, vector2)

                print(cosine, count)

#arq1 = open("CERN-_-TIGRE.txt", "r")
#arq1line = arq1.read()
#arq2 = open("bids-standard-_-bids-starter-kit.txt", "r")
#arq2line = arq2.read()
#print(len(arq2line.split()))
