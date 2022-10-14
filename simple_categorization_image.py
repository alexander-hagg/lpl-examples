# 1. Single pixel categorizer, with fixed threshold
# 2. Image categorizer, with fixed threshold
# 3. Random threshold
# 4. Training: give examples and nudge random init threshold towards correct labeling

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def singlepixel_categorizer(pixel, threshold=0.6):
    if pixel > threshold:
        return 1
    else:
        return 0

def image_categorizer(img_array):
    categories = np.zeros(img_array.shape)
    for x in range(img_array.shape[0]):
        for y in range(img_array.shape[1]):
            pixel = img_array[x][y]
            category = singlepixel_categorizer(pixel)
            categories[x][y] = category
    return categories


image_location = 'img/forestfloor.jpg'
img = Image.open(image_location).convert('L')
img_arr = np.array(img, np.uint8)
img_arr = img_arr/255
categories = image_categorizer(img_arr)
print(f'categories: {categories}')
plt.imshow(categories, cmap='gray')
# img = Image.fromarray(img_arr)
# plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
