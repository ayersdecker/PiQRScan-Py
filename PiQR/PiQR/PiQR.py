# Import Camera functions from cv2
# Import QR functions from pyzbar
import cv2
import numpy as np
import pyzbar.pyzbar as qr

# Holds Camera Feed
cap=cv2.VideoCapture(0)
# Used in displayed text
font = cv2.FONT_HERSHEY_PLAIN

# Main Loop
while True:
    # Proccess Frame
      ret,frame = cap.read()
      flipped = cv2.flip(frame, flipCode=-1)
      frame1=cv2.resize(flipped,(640,480))
    # Scan Frame
      qrdetect=qr.decode(frame1)

    # Paste Green Frame on QR
      for i in qrdetect:
          print (i.rect.left,i.rect.top,i.rect.width,i.rect.height)
          print (i.data)
          cv2.rectangle(frame1,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,255,0),3)
          cv2.putText(frame1,str(i.data),(20,20),font,2,(255,0,0),2) 
      cv2.imshow("Frame", frame1)
      key = cv2.waitKey(1) & 0xFF
    # Press q to quit 
      if key == ord("q"):
         break

# Editting this code from https://github.com/freedomwebtech/rpiqrcodescanner/blob/main/qr.py 
# Not complete yet, I do not take credit for the code above.