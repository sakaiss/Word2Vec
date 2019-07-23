import codecs
import re
import os
import sys
import jieba

f=codecs.open('lastread.txt', "a+",'utf-8')
for line in open("wiki.zh.jian.text"):
    for i in re.sub('[a-zA-Z0-9]','',line).split(' '):
        if i!='':
            data=list(jieba.cut(i,cut_all=False))
            readline=' '.join(data)+'\n'
            f.write(readline)
f.close()

