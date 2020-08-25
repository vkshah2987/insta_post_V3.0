from linkpreview import link_preview
import googlenews


#link = link_preview(googlenews.links("virtual reality"), parser = "lxml")
#print(link)
#link = link_preview("https://news.google.com/articles/CAIiEC1pN1aK6Zhf453lYYLY0h4qGAgEKg8IACoHCAow3rvTBDD89X4wsLbmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen", parser="lxml")
def title(tt):
    link = link_preview(tt, parser = "lxml")
    #print("title:", link.title)
    return link.title

def desc(ds):
    link = link_preview(ds, parser = "lxml")
    print("description:", link.description)
    return link.description

def image(im):
    link = link_preview(im, parser = "lxml")
    #print("image:", link.image)
    return link.image


#print("force_title:", preview.force_title)
#print("absolute_image:", preview.absolute_image)