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
    # img = qrcode.make(url)
    # imgurl = settings.MEDIA_ROOT + "/cert/" + code + '.png'
    return img


def generateCert(request, type, code, name, gender, unit, grade, title, avai_year, avai_mouth, avai_day, user,
                 avatar=None, b64=False):
    curr_time = datetime.datetime.now()
    localdate = curr_time.strftime("%Y-%m-%d").split("-")
    projectpath = os.path.abspath('.') + "/apps/certification/static/"
    # projectpath = os.path.abspath('.') + "/static/"
    image = Image.open(projectpath + 'cert.jpg')

    fontPath = projectpath + "msyh.ttf"
    setFont = ImageFont.truetype(fontPath, 70)
    dateFont = ImageFont.truetype(fontPath, 50)
    draw = ImageDraw.Draw(image)
    draw.text((710, 260), type, fill="black", font=setFont)
    draw.text((710, 400), code, fill="black", font=setFont)
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
        # base64_data = re.sub('^data:image/.+;base64,', '', avatar)
        if b64:
            byte_data = base64.b64decode(avatar)
            image_data = BytesIO(byte_data)
            avatar = Image.open(image_data).convert("CMYK")
        else:
            print(avatar)
            avatar = Image.open(avatar)
        avatar = avatar.resize((400, 560))
        image.paste(avatar, (585, 1525))
    else:
        avatar = Image.open(projectpath + "defaultavatar.jpg").convert("CMYK")
        avatar = avatar.resize((400, 560))
        image.paste(avatar, (585, 1525))

    QR = generateQRcode(user, request.get_host())
    QR.resize((1200,1200))
    image.paste(QR, (500, 2400))
    output_buffer = BytesIO()
    image.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    # image.show()
    return base64_str


# generateCert(None, "jxg20120001", "普通会员", "邓晓华", "男", "南昌大学", "二级", "教授", "2020", "11", "20", "1")
