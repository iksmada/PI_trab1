import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from os import listdir, path, makedirs
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


# select randonly a image from dirName
dirName = 'imagens_objetos_coloridos'
images = listdir(dirName)
imgName = images[np.trunc(np.random.rand() * len(images)).astype(int)]
completeFilePath = dirName + '/' + imgName
img = cv2.imread(completeFilePath)
img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# define plot images grid
fig = plt.figure()
row = 2
column = 2
figCounter = 1

# ensure save path exists
fileName = path.splitext(imgName)
resultsDirName = dirName + '_results'
if not path.isdir(resultsDirName):
    makedirs(resultsDirName)

# plot original image
cv2.imshow('Original', img)
cv2.waitKey(1000)

# plot and save bw image
binary = im_bw = cv2.threshold(img_greyscale, 254, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('Black n\' White', binary)
cv2.imwrite(resultsDirName + '/' + fileName[0] + '_' + 'bw' + fileName[1], binary)
cv2.waitKey(1000)

edges = ~cv2.Canny(np.uint8(binary), 100, 200)
cv2.imshow('Edge Image', edges)
cv2.imwrite(resultsDirName + '/' + fileName[0] + '_' + 'edges' + fileName[1], edges)
cv2.waitKey(1000)

# show grid of images
plt.tight_layout()
plt.show()