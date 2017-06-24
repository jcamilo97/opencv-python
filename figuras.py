import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# ima,corint, coorend,color,width line
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#top-left corner and bottom-right corner of rectangle =
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#coor_central , radio
img = cv2.circle(img,(447,63), 63, (0,0,255),-1)
#coor_central, (width,heigth),rotation,angle_init,angle_end, -->in anti-clockwise direction 
img = cv2.ellipse(img,(256,256),(100,10),0,0,180,(0,255,0),-1)
#polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
#text, coor top-left-corner, font,font scale, color, grosor, ?
cv2.putText(img,'OpenCV',(10,490), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('figure.png',img)
    cv2.destroyAllWindows()