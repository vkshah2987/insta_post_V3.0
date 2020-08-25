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


print(""" 1. Technology              2. Machine Learning             3. Mobile \n 4. Data Science            5. NASA                         6. Crypto Currency
 7. Microsoft               8. Apple Inc                    9. Virtual Reality \n10. AR                     11. SpaceX                      12. Tesla
13. Gadget                 14. Robotic                     15. Amazon\n16. Flipkart               17. Internet                    18. Cyber Security
19. AI                     20. Blockchain                  21. Cloud\n22. IoT                    23. Social Media                24. Edge Computing
25. Custom""")
def main():
    #time = datetime.datetime.now()
    t = input("Enter your choice: ")
    #print(t)
    if str(t) == "1":
        cat("technology", "TECH")
        remove()
    elif str(t) == "2":
        cat("machine learning", "ML")
        remove()
    elif str(t) == "3":
        cat("mobile", "MOBILE")
        remove()
    elif str(t) == "4":
        cat("data science", "DS")
        remove()
    elif str(t) == "5":
        cat("nasa", "NASA")
        remove()
    elif str(t) == "6":
        cat("crypto currency", "CRYPTO")
        remove()
    elif str(t) == "7":
        cat("microsoft", "MICROSOFT")
        remove()
    elif str(t) == "8":
        cat("apple inc", "APPLE")
        remove()
    elif str(t) == "9":
        cat("VR", "VIRTUAL REALITY")
        remove()
    elif str(t) == "10":
        cat("argumented reality", "AR")
        remove()
    elif str(t) == "11":
        cat("spacex", "SPACEX")
        remove()
    elif str(t) == "12":
        cat("tesla", "TESLA")
        remove()
    elif str(t) == "13":
        cat("Gadgets", "GADGET")
        remove()
    elif str(t) == "14":
        cat("robotics", "ROBOTIC")
        remove()
    elif str(t) == "15":
        cat("amazon", "AMAZON")
        remove()
    elif str(t) == "16":
        cat("flipkart", "FLIPKART")
        remove()
    elif str(t) == "17":
        cat("internet", "INTERNET")
        remove()
    elif str(t) == "18":
        cat("cyber security", "CYBER")
        remove()
    elif str(t) == "19":
        cat("artificial intelligence", "AI")
        remove()
    elif str(t) == "20":
        cat("blockchain", "BLOCKCHAIN")
        remove()
    elif str(t) == "21":
        cat("cloud computer", "CLOUD")
        remove()
    elif str(t) == "22":
        cat("internet of thing", "IoT")
        remove()
    elif str(t) == "23":
        cat("social media", "SOCIAL MEDIA")
        remove()
    elif str(t) == "24":
        cat("edge computing", "EDGE-COMP")
        remove()
    elif str(t) == "25":
        topic = input("Enter the topic: ")
        head = input("Enter the header: ")
        cat(topic,head)
        remove()




main()