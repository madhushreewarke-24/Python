
!pip install qrcode

import qrcode as qr
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=3,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=80,border=4)

link=input("Enter the Link : ")
img = qr.make(link)

img=qr.make_image(fill_color="navy",back_color="ivory")

img.save("Image.png")
