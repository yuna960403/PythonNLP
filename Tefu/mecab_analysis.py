import MeCab
import wc
from collections import Counter

text = wc.text

mecab = MeCab.Tagger ('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
result = mecab.parse(text)

lines = result.split("\n")
words = []

for line in lines :
    feature = line.split("\t")
    if len(feature) == 2 :
        info = feature[1].split(",")
        if info[0] == "名詞" :
            words.append(info[6])

cnt = Counter(words)
print(cnt.most_common)