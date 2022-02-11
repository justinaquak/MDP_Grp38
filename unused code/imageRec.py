import ftplib
import picamera
from time import sleep

# Taking Image
camera= picamera.PiCamera()
camera.capture('image1.jpg')
session=ftplib.FTP('192.168.38.1','bebe','1111') #PC ip means windows pc ip
file = open('/home/pi/image1.jpg','rb')
session.storbinary('STOR image.jpg',file)
file.close()
session.quit()