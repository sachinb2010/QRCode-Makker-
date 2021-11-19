import pyqrcode
import png
from pyqrcode import QRCode

website=input("Please insert website herer with")
qr="website"
url=pyqrcode.create(qr)
url.svg("YourQR.svg",scale=8)
url.png("YourQR.png",scale=6)