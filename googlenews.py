from GoogleNews import GoogleNews
import os

def links(search):
    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews.search(search)
    x = googlenews.get__links()
    f1 = open("picst.txt","r")
    p = f1.read()
    f1.close()

    for i in x:
        if i in p:
            continue
        elif i == None:
            continue
        else:
            f2 = open("picst.txt","a")
            f2.write(i+"\r\n")
            f2.close
            return i

#print(links("hello world"))