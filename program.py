import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")
def detect_circle(img):
    crop = img[50:350, 310:660]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.blur(gray,(4,5))
    detecting_cirlcles = cv2.HoughCircles(blur_image,cv2.HOUGH_GRADIENT,1,30,param1 = 30, param2 = 30, minRadius = 1, maxRadius = 46)
    count = 0
    if detecting_cirlcles is not None :
        detecting_circles = np.uint16(np.around(detecting_cirlcles))
        for i in detecting_cirlcles[0,:]:
            a,b,r=i[0],i[1],i[2]
            cv2.circle(crop,(int(a),int(b)),int(r),(0,255,0),2)
            count = count + 1
    return count, img
img = cv2.imread('OpenCV_Assignment_Image.png',cv2.IMREAD_COLOR)
count,img = detect_circle(img)
print("Total Wood Log : ",count)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()