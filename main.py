import datetime
import os
from time import sleep
import img_olp as io
import material as mt
import txt_wrp as tw
import googlenews as gn
import Download_Image as di
import instagram as ig

def cat(search, text):
    #search = "spacex"
    lk = gn.links(search)
    ttl = mt.title(lk)
    img = mt.image(lk)
    tw.draw_text(ttl)
    di.image_down(img)
    io.pic()
    io.final()
    io.body()
    io.title(text)
    ds = mt.desc(lk)
    ig.post(ds,text)



def remove():
    file = ["local_image.png","pic_body.jpg","pic_layout.jpg","pic_line.png","word2.png","pic_done.jpg.REMOVE_ME"]
    for i in file:
        os.remove(i)
        print(i)



while True:
    time = datetime.datetime.now()
    t = str(time.hour)+":"+str(time.minute)
    print(t)
    if str(t) == "9:0":
        cat("technology", "TECH")
        remove()
        sleep(100)
        continue
    elif str(t) == "9:31":
        cat("machine learning", "ML")
        remove()
        sleep(100)
        continue
    elif str(t) == "10:0":
        cat("mobile", "MOBILE")
        remove()
        sleep(100)
        continue
    elif str(t) == "10:31":
        cat("data science", "DS")
        remove()
        sleep(100)
        continue
    elif str(t) == "11:0":
        cat("nasa", "NASA")
        remove()
        sleep(100)
        continue
    elif str(t) == "11:31":
        cat("crypto currency", "CRYPTO")
        remove()
        sleep(100)
        continue
    elif str(t) == "12:0":
        cat("microsoft", "MICROSOFT")
        remove()
        sleep(100)
        continue
    elif str(t) == "12:31":
        cat("apple inc", "APPLE")
        remove()
        sleep(100)
        continue
    elif str(t) == "13:0":
        cat("VR", "VIRTUAL REALITY")
        remove()
        sleep(100)
        continue
    elif str(t) == "13:31":
        cat("argumented reality", "AR")
        remove()
        sleep(100)
        continue
    elif str(t) == "14:0":
        cat("spacex", "SPACEX")
        remove()
        sleep(100)
        continue
    elif str(t) == "14:31":
        cat("tesla", "TESLA")
        remove()
        sleep(100)
        continue
    elif str(t) == "15:0":
        cat("Gadgets", "GADGET")
        remove()
        sleep(100)
        continue
    elif str(t) == "15:31":
        cat("robotics", "ROBOTIC")
        remove()
        sleep(100)
        continue
    elif str(t) == "16:0":
        cat("amazon", "AMAZON")
        remove()
        sleep(100)
        continue
    elif str(t) == "16:31":
        cat("flipkart", "FLIPKART")
        remove()
        sleep(100)
        continue
    elif str(t) == "17:0":
        cat("internet", "INTERNET")
        remove()
        sleep(100)
        continue
    elif str(t) == "17:31":
        cat("cyber security", "CYBER")
        remove()
        sleep(100)
        continue
    elif str(t) == "18:0":
        cat("artificial intelligence", "AI")
        remove()
        sleep(100)
        continue
    elif str(t) == "18:31":
        cat("blockchain", "BLOCKCHAIN")
        remove()
        sleep(100)
        continue
    elif str(t) == "19:0":
        cat("cloud computer", "CLOUD")
        remove()
        sleep(100)
        continue
    elif str(t) == "19:31":
        cat("internet of thing", "IoT")
        remove()
        sleep(100)
        continue
    elif str(t) == "20:0":
        cat("social media", "SOCIAL MEDIA")
        remove()
        sleep(100)
        continue
    elif str(t) == "20:36":
        cat("edge computing", "EDGE-COMP")
        remove()
        sleep(100)
        continue