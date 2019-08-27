from glob import glob                                                           
import cv2 
jpgs = glob('./*.JPG')

for j in jpgs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'png', img)