from PIL import Image, ImageDraw, ImageFont
import datetime
from django.conf import settings
import base64
import re
from io import BytesIO


def generateCert(type, code, name, gender, unit, grade, title, avai_year, avai_mouth, avai_day, avatar=None):
    curr_time = datetime.datetime.now()
    localdate = curr_time.strftime("%Y-%m-%d").split("-")
    image = Image.open('assets/cert.jpg')

    fontPath = "assets/msyh.ttf"
    setFont = ImageFont.truetype(fontPath, 70)
    dateFont = ImageFont.truetype(fontPath, 50)
    draw = ImageDraw.Draw(image)
    draw.text((700, 260), type, fill="black", font=setFont)
    draw.text((700, 400), code, fill="black", font=setFont)
    draw.text((1290, 1500), name, fill="black", font=setFont)
    draw.text((1290, 1630), gender, fill="black", font=setFont)
    draw.text((1430, 1760), unit, fill="black", font=setFont)
    draw.text((1430, 1890), grade, fill="black", font=setFont)
    draw.text((1290, 2010), title, fill="black", font=setFont)
    draw.text((1230, 2295), avai_year, fill="black", font=dateFont)
    draw.text((1450, 2295), avai_mouth, fill="black", font=dateFont)
    draw.text((1600, 2295), avai_day, fill="black", font=dateFont)
    draw.text((1660, 2805), localdate[0], fill="black", font=dateFont)
    draw.text((1870, 2805), localdate[1], fill="black", font=dateFont)
    draw.text((2010, 2805), localdate[2], fill="black", font=dateFont)
    if avatar:
        base64_data = re.sub('^data:image/.+;base64,', '', avatar)
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        avatar = Image.open(image_data).convert("CMYK")
        avatar = avatar.resize((400, 560))
        image.paste(avatar, (585, 1525))
    else:
        avatar = Image.open("assets/defaultavatar.jpg").convert("CMYK")
        avatar = avatar.resize((400, 560))
        image.paste(avatar, (585, 1525))
    output_buffer = BytesIO()
    image.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str
