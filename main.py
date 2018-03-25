import numpy as np
from os import listdir, path, makedirs
import cv2

# select randonly a image from dirName
dirName = 'imagens_objetos_coloridos'
images = listdir(dirName)
imgName = images[np.trunc(np.random.rand() * len(images)).astype(int)]
completeFilePath = dirName + '/' + imgName
img = cv2.imread(completeFilePath)
img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ensure save path exists
fileName = path.splitext(imgName)
resultsDirName = dirName + '_results'
if not path.isdir(resultsDirName):
    makedirs(resultsDirName)

# plot original image
cv2.imshow('Original', img)
cv2.waitKey(1000)

# plot and save bw image
binary = cv2.threshold(img_greyscale, 254, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('Black n\' White', binary)
cv2.imwrite(resultsDirName + '/' + fileName[0] + '_' + 'bw' + fileName[1], binary)
cv2.waitKey(1000)

# plot and save edges image
edges = ~cv2.Canny(np.uint8(binary), 100, 200)
cv2.imshow('Edge Image', edges)
cv2.imwrite(resultsDirName + '/' + fileName[0] + '_' + 'edges' + fileName[1], edges)
cv2.waitKey(1000)

#numbered image and stats
image, contours, hierarchy = cv2.findContours(binary, 1, 2)
del contours[-1]
i=0
font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 0.5
fontColor              = (255,255,255)
lineType               = 1
for cnt in contours:
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(binary, str(i),
                (cx-8,cy+5),
                font,
                fontScale,
                fontColor,
                lineType)
    print("região: %2d   perímetro: %7.2f   área: %6d" % (i, cv2.arcLength(cnt,True), cv2.contourArea(cnt)))
    i = i+1

cv2.imshow('Centroids', image)
cv2.imwrite(resultsDirName + '/' + fileName[0] + '_' + 'centroids' + fileName[1], image)
cv2.waitKey(20000) & 0xFF

