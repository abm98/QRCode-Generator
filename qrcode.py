import pyqrcode
import png
image = pyqrcode.create("https://youtu.be/09fpBobFKqQ")
image.svg("rekhta.svg")
image.png("rekhta.png")
