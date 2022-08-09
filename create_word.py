'''Сколько слов можно составить из букв заданного слово'''

import re
file=open('C:\\Users\\Aleksandr\\Desktop\\python26\\russian.txt','r')

final=[]
list_new_word=[]

list=[line.rstrip() for line in file]
for word in list:
    sp=re.split(r"[^ростелеком]+"ord)
    if len(sp)==1:
        list_new_word.append(word)
for i in list_new_word:
    if i in list:
        final.append(i)
    else:
        continue
print (final)





out=open('C:\\Users\\Aleksandr\\Desktop\\python26\\new_word.txt','w')
out.write(f'Составленные слова из заданного слова \n')
for i in list_new_word:
    out.write(f'{i}\n')
out.close()   