import os
from wordseg import WordSegment


dic = []
new = set()
text = ""
with open("dict/dict.txt", encoding="utf-8") as fin:
    for i in fin.readlines():
        dic.append(i)


with open("icwb2-data/testing/msr_test.utf8", encoding="utf-8") as fin:
    text = text + fin.read()
with open("icwb2-data/testing/pku_test.utf8", encoding="utf-8") as fin:
    text = text + fin.read()

ws = WordSegment(text, max_word_len=4, min_aggregation=150, min_entropy=2)
for w in ws.words:
    w = w.strip() + "\n"
    if w not in dic:
        new.add(w)

savepath = "dict/wordseg.txt"
with open(savepath, mode="w", encoding="utf-8") as fout:
    for d in new:
        fout.write(d)
    for d in dic:
        fout.write(d)
