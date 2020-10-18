from PIL import Image, ImageDraw, ImageFont
import datetime
from django.conf import settings
import base64
import re
import qrcode
from io import BytesIO
import os


def generateQRcode(code, host):
    url = host + "/api/cert/" + str(code) + "/"
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=13,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    return img


def generateCert(request, type, code, name, unit, edu, profession, level, title, avai_year, avai_mouth, avai_day,
                 avatar=None, b64=False):
    curr_time = datetime.datetime.now()
    projectpath = os.path.abspath('.') + "/apps/certification/static/"
    # projectpath = os.path.abspath('.') + "/static/"
    if type == "普通会员":
        image = Image.open(projectpath + 'commonCert.jpg')
    elif type == "高级会员":
        image = Image.open(projectpath + 'seniorCert.jpg')
    starttime = datetime.datetime.now()
    fontPath = projectpath + "msyh.ttf"
    setFont = ImageFont.truetype(fontPath, 60)
    dateFont = ImageFont.truetype(fontPath, 55)
    draw = ImageDraw.Draw(image)
    draw.text((980, 2310), code, fill="black", font=setFont)
    draw.text((1280, 1500), name, fill="black", font=setFont)
    draw.text((1430, 1630), unit, fill="black", font=setFont)
    draw.text((1280, 1760), edu, fill="black", font=setFont)
    draw.text((1280, 1880), profession, fill="black", font=setFont)
    draw.text((1660, 2010), level, fill="black", font=setFont)
    draw.text((1280, 2130), title, fill="black", font=setFont)
    draw.text((1600, 2790), avai_year, fill="black", font=dateFont)
    draw.text((1810, 2790), avai_mouth, fill="black", font=dateFont)
    draw.text((1990, 2790), avai_day, fill="black", font=dateFont)
    # draw.text((1660, 2805), localdate[0], fill="black", font=dateFont)
    # draw.text((1870, 2805), localdate[1], fill="black", font=dateFont)
    # draw.text((2010, 2805), localdate[2], fill="black", font=dateFont)
    if avatar:
        # base64_data = re.sub('^data:image/.+;base64,', '', avatar)
        if b64:
            byte_data = base64.b64decode(avatar)
            image_data = BytesIO(byte_data)
            avatar = Image.open(image_data).convert("CMYK")
        else:
            avatar = Image.open(avatar)
        avatar = avatar.resize((430, 590))
        image.paste(avatar, (575, 1565))
    else:
        avatar = Image.open(projectpath + "defaultavatar.jpg").convert("CMYK")
        avatar = avatar.resize((430, 590))
        image.paste(avatar, (575, 1565))

    QR = generateQRcode(request.user.id, request.get_host())
    # QR = generateQRcode("14", "127.0.0.1")

    QR.resize((1200, 1200))
    image.paste(QR, (500, 2500))
    output_buffer = BytesIO()
    image.save(output_buffer, format='jpeg')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    # image.save("test.png")
    return base64_str


# generateCert(None, "高级会员", "jsg20120233", "张立东", "江西省检察院", "本科", "法律", "二级", "高级检察官", "2020", "8", "1")
