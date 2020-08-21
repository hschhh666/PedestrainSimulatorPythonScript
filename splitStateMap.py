import numpy as np
import cv2

imgFile = 'D:/IV2020MapPrediction/paper/stateMapSample1.jpg'

img = cv2.imread(imgFile)
cols = np.shape(img)[0]
rows = np.shape(img)[1]




img = cv2.resize(img,(int(rows*0.4),int(cols*0.4)))
cv2.imshow('img',img)
cv2.waitKey(0)

print(cols,rows)