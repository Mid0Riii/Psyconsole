from django.test import TestCase

# Create your tests here.
import qrcode
from PIL import Image, ImageDraw, ImageFont
import datetime

#
# image = Image.open('assets/cert.jpg')
#
# def get_size(image):
#     #获取图像的宽和高
#     width, height = image.size
#     return width,height
#
# setFont = ImageFont.truetype("assets/msyh.ttf",20)
# print(get_size(image))
# draw = ImageDraw.Draw(image)
# draw.text((200,100),"测试",fill="black",font=setFont)
# image.show()
# # img = qrcode.make('http://www.baidu.com')
# # with open('test.png', 'wb') as f:
# #     img.save(f)
def generateCert(type, code, name, gender, unit,grade,title,avai_year,avai_mouth,avai_day,avatar):
    curr_time = datetime.datetime.now()
    localdate = curr_time.strftime("%Y-%m-%d").split("-")
    image = Image.open('assets/cert.jpg')

    fontPath = "assets/msyh.ttf"
    setFont = ImageFont.truetype(fontPath, 70)
    dateFont = ImageFont.truetype(fontPath,50)
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

    avatar = Image.open("assets/defaultavatar.jpg").convert("CMYK")
    avatar = avatar.resize((400,560))
    image.paste(avatar,(585,1525))


    image.show()


generateCert("37373737373737", "普通会员", "张三", "男", "南昌大学", "二级", "讲师", "2020","11","20","" )
