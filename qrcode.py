import pyqrcode
import png
# Provide the link below of any site which you want to convert in QR Code 
image = pyqrcode.create("https://youtu.be/09fpBobFKqQ")
image.svg("rekhta.svg")
image.png("rekhta.png")
# Save and Run You Will get the file in the same location where your py file is save
