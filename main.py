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
img = mpimg.imread(dirName + '/' + imgName, True)

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
a = fig.add_subplot(row, column, figCounter)
figCounter = figCounter + 1
plt.imshow(img, vmin=0, vmax=255)
a.set_title('Original')


# plot and save negative image
a = fig.add_subplot(row, column, figCounter)
figCounter = figCounter + 1
gray=rgb2gray(img)
binary = ~(gray<255)
#gray = (bolleanImg[:,:,0]|bolleanImg[:,:,1]|bolleanImg[:,:,2])
plt.imshow(binary, cmap='binary_r')
a.set_title('Black n\' White')
extent = a.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(resultsDirName + '/' + fileName[0] + '_' + 'bw' + fileName[1], bbox_inches=extent)


# show grid of images
plt.tight_layout()
plt.show()