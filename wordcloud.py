import collections
import string
f=open('98.txt',encoding="utf8")
f2=open('stopwords.txt',"r",encoding="utf8")
c=f2.read().split('\n')

wc={}


for word in f.read().lower().split():
     word=word.replace(".","")
     word= word.replace(",","")
     word=word.replace("\"","")
     word=word.replace('"',"")
     if word not in c:
        if word not in wc:
            wc[word]=1
        else:
                wc[word]+=1


d=collections.Counter(wc)
for word,count in d.most_common(10):
    print(word,":", count)




    
    
