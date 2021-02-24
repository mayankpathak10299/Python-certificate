from PIL import Image, ImageFont, ImageDraw
import pandas as pd

FONT_FILE = ImageFont.truetype(r'GreatVibes-Regular.ttf', 100)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 805,675


def make_cert(name):
    image_source = Image.open(r'CER.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH - name_width / 2, HEIGHT - name_height / 2), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + name + ".jpg")
    print('printing certificate of: ' + name)


data=pd.read_excel('sheet.xlsx')
names = list(data.Name)
for x in names:
    make_cert(x)
