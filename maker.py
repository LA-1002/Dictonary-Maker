from audioop import mul
import enchant;
import itertools
import string;
import multiprocessing


d = enchant.Dict('en_UK')

def createDict(num):
    fileA = open('%iLetter_Wordlist.txt'%num,'a',encoding='utf-8')
    for w in itertools.product(string.ascii_lowercase, repeat=num):
        word = (''.join(w))
        if (d.check(word)== True):
            print(word)
            fileA.write(word + '\n')
    fileA.close();



