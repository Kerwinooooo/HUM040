import io
import sys
import time

import pandas as pd
from wordseg import WordSegment
import pkuseg
import difflib

jiebaWordSet = set()
fileName = ''
newWordFileName = ''

def getText() -> str:
    global fileName
    inputText = input("text or file path:")
    try:
        file = open(file=inputText, mode='r', encoding='utf-8')
        text = file.read()
        file.close()
        fileName = inputText.rsplit('.')[0]
        return text
    except Exception as e:
        print(e)
        return inputText


def init():
    # 改变标准输出的默认编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    loadJiebaWordSet()



def loadJiebaWordSet():
    global jiebaWordSet
    df = pd.read_excel('jiebaWordlist.xlsx')
    jiebaData = df.values
    jiebaWordSet = set(row[0] for row in jiebaData)


def getNewWordList(orgText: str) -> list:
    global newWordFileName
    newWordList = []
    ws = WordSegment(orgText, max_word_len=10, min_freq=0.00005, min_entropy=0.4, min_aggregation=1.2)

    for word in ws.words:
        if word not in jiebaWordSet and ' ' not in word:  # remove the 'new word' that contains space
            newWordList.append(word)
            # print(word)

    newWordFileName = fileName + '_newWord_' + str(int(time.time())) + '.txt'
    file = open(file=newWordFileName, mode='w', encoding='utf-8')
    file.write('\n'.join(newWordList))
    file.close()

    return newWordList


def segment():
    segWithoutNewWord = pkuseg.pkuseg()
    resultWithoutNewWord = segWithoutNewWord.cut(orgText)
    file = open(file=fileName + '_result_without_new_word_' + str(int(time.time())) + '.txt', mode='w', encoding='utf-8')
    file.write(' '.join(resultWithoutNewWord))
    file.close()

    segWithNewWord = pkuseg.pkuseg(user_dict=newWordFileName)
    resultWithNewWord = segWithNewWord.cut(orgText)
    file = open(file=fileName + '_result_with_new_word_' + str(int(time.time())) + '.txt', mode='w', encoding='utf-8')
    file.write(' '.join(resultWithNewWord))
    file.close()

    # d = difflib.Differ()
    # diff = d.compare(' '.join(resultWithoutNewWord), ' '.join(resultWithNewWord))
    # print('\n'.join(diff))


if __name__ == '__main__':
    init()

    orgText = getText()
    # print(f'orgText: {orgText}')

    timeNewwordStart = time.time()
    getNewWordList(orgText)
    print(f'getNewWordList: {time.time() - timeNewwordStart}')
    # print(f'new words: {" ".join(jiebaWordSet)}')

    timeSegmentStart = time.time()
    segment()
    print(f'segment: {time.time() - timeSegmentStart}')

    print('finished')
