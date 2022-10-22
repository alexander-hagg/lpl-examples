# The I/O module is used for importing the image  
import numpy as np  
import matplotlib.pyplot as plt
import skimage.data as data  
import skimage.segmentation as seg  
import skimage.filters as filters  
import skimage.draw as draw  
import skimage.color as color
from skimage import io

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

image = io.imread('bear.jpg')
image_felzenszwalb = seg.felzenszwalb(image)   
image_show(image_felzenszwalb)
plt.show()
image_felzenszwalb_colored = color.label2rgb(image_felzenszwalb, image, kind='avg')
image_show(image_felzenszwalb_colored)
plt.show()

