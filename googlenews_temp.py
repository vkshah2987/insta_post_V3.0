from GoogleNews import GoogleNews

def links(search):
    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews.search(search)
    x = googlenews.get__links()
    return x[0]

#print(links("virtual reality"))
