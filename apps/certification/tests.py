from django.test import TestCase

# Create your tests here.
import qrcode

img = qrcode.make('http://www.baidu.com')
with open('test.png', 'wb') as f:
    img.save(f)