from pathlib import Path
from itertools import islice
import os

def sortFileByTime():
    dirpath = 'docs/'
    path = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
    res = list(islice(reversed(path), 0, 2))
    res.reverse()
    return res

def getFileName(res):
    mylist = []
    for x in res:
        filename = os.path.basename(x)
        mylist.append(filename)
    return mylist

def getHarmony(mylist):
    for file in mylist:
        if file.startswith('SHY'):
            return file

def getTaylorCreek(mylist):
    for file in mylist:
        if file.startswith('STC'):
            return file