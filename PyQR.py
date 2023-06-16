######################################################################
# How to install depedencies in Python ###############################
######################################################################
# sudo apt-get update
# sudo apt-get install python-qrtools

# [sudo] pip install pypng
# [sudo] pip install zbar
# [sudo] pip install pillow

######################################################################
# Python program to generate QR code #################################
######################################################################  
from qrtools import QR
  
import os
my_QR = QR(data = u"Example")
my_QR.encode()
  
# command to move the QR code to the desktop
os.system("sudo mv " + my_QR.filename + " ~/Desktop")

######################################################################
# Python program to Scan and Read a QR code ##########################
######################################################################
from qrtools import QR
my_QR = QR(filename = "home/user/Desktop/qr.png")
  
# decodes the QR code and returns True if successful
my_QR.decode()
  
# prints the data
print (my_QR.data)