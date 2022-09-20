import cv2
import numpy as np
import math
import keyboard
xa = 320
xy = 240
sayac=0
uzaklik=0
kamera=cv2.VideoCapture(0)
#mask1 = cv2.inRange(frame_hsv, (0, 70, 50), (10, 255, 255))
#  mask2 = cv2.inRange(frame_hsv, (160, 70, 50), (180, 255, 255))
#  mask = mask1 + mask2
def deneme():
    while True:
        a, goruntu = kamera.read()
        hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
        frame = cv2.bilateralFilter(hsv,9,75,75)
        mask1 = cv2.inRange(frame, (0, 140, 50), (6, 255, 255))
        mask2 = cv2.inRange(frame, (35, 170, 50), (185, 255, 255))
        mask = mask1 + mask2
        white_pixels = np.where(mask == 255)
        if len(white_pixels[0]) > 9000:
           print("lüt")
        daire = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,goruntu.shape[0]/2,param1=200,param2=10,minRadius=1,maxRadius=50) # çözünürlük değreri,min mesafe,metoda özel değerler param1,param2,minimum yarçap ,mak yarı çap)
        if daire is not None:  # NONE DAN FARKLIYSA BOŞ DEĞİLSE
           daire = np.uint16(np.around(daire)) # değer yuvarlama
           cv2.putText(goruntu,"ALGILANDI",(480,480),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
           M = cv2.moments(mask)
           x = int(M["m10"] / M["m00"])  # merkezin x, y koordinatlarını hesaplama
           y = int(M["m01"] / M["m00"])
           for i in daire[0, :]:
              cv2.circle(goruntu,(i[0],i[1]),i[2],(255,255,255),2) # yuvarlak içine alma#merkezi# #yarıçap
              cv2.circle(goruntu,(x,y),5,(128,128,255),-1)
              cv2.line(goruntu,(x,y),(xa,xy),(255,255,255),2)
              cv2.putText(goruntu, "Cisim Merkezi", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
              #sayacı say aralıklarını belirle ordaysa at
        #cv2.circle(goruntu, (xa,xy), 3, (32, 178, 170), 4)
           sonuc1=(x-xa)
           sonuc2=(y-xy)
           uzaklik=math.sqrt((sonuc1*sonuc1)+(sonuc2*sonuc2))
           cv2.circle(goruntu,(xa,xy), 9, (128,128,0),-1)
           cv2.putText(goruntu,"Kamera Merkezi", (200, 300),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
           cv2.putText(goruntu,"Uzaklik :{}".format(int(uzaklik)),(250,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255,255), 1)
           if uzaklik < 15 or uzaklik < 90:#ayarla
               '''
               enlem=vehicle.location.global_relative_frame.lat
               boylam=vehicle.location.global_relative_frame.lon
               print(enlem,"  ",boylam)
               '''
               cv2.putText(goruntu, "ALANDA", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
          # mask=cv2.inRange(goruntu,dusuk,yuksek
           cv2.imshow("renkli",goruntu)
           if cv2.waitKey(25) & 0xFF == ord('q'):
              break
deneme()
kamera.release()
cv2.destroyAllWindows()