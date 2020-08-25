from PIL import Image, ImageFont, ImageDraw


"""def rot(img):
    img = img.rotate(90, expand = 1)
    return img"""

def body():
    img = Image.open("pic_line.png")
    img2 = Image.open("word2.png")
    img.paste(img2, (20,210))
    img.save("pic_body.jpg")


def final():
    ironman = Image.open("Final_Layout.png")
    bg = Image.open("pic_layout.jpg")
    text_img = Image.new('RGB', (960,540), (0, 0, 0, 0))
    text_img.paste(bg, (0,0))
    text_img.paste(ironman, (0,0), mask=ironman)
    text_img.save("pic_line.png", format="png")


def pic():
    img = Image.open("Background_Layout.jpg")
    img2 = Image.open("local_image.png") 
    img2 = img2.resize((719, 405))
    img.paste(img2, (215,95))
    img.save("pic_layout.jpg")


def title(ttl):
    img = Image.open("pic_body.jpg")
    #text = "Hello World"
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Quicksand-Bold.ttf', 35)
    draw.text((465, 28), ttl, (255, 255, 255), font=font)
    img.save("pic_done.jpg")