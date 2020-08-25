# Import requests, shutil python module.
import requests
import shutil

def image_down(image_url):
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open('local_image.png', 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp


#image_down("https://primefeed.in/news/3766118/virtual-reality-gaming-accessories-market-from-key-end-use-sectors-to-surge-in-the-near-future/")