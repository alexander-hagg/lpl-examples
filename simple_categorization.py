# 1. Single pixel categorizer, with fixed threshold
# 2. Image categorizer, with fixed threshold
# 3. Random threshold
# 4. Training: give examples and nudge random init threshold towards correct labeling

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def singlepixel_categorizer(pixel_array, threshold=0.5):
    category_labels = ['dunkel', 'hell']
    # Categorize grayscale pixel
    if pixel_array[0][0] > threshold:
        category = 1
    else:
        category = 0
    return category_labels[category]

def image_categorizer(img):
    pass

image_location = 'img/white.png'
# Open and convert to grayscale
img = Image.open(image_location).convert('L')
# Convert to numpy array
img_arr = np.array(img, np.uint8)
category = singlepixel_categorizer(img_arr)
print(f'category: {category}')

image_location = 'img/black.png'
img = Image.open(image_location).convert('L')
img_arr = np.array(img, np.uint8)
category = singlepixel_categorizer(img_arr)
print(f'category: {category}')

image_location = 'img/forestfloor.jpg'
img = Image.open(image_location) # .convert('L')
img_arr = np.array(img, np.uint8)
img_arr = img_arr[::, ::, 2]
category = singlepixel_categorizer(img_arr)
print(f'category: {category}')
img = Image.fromarray(img_arr)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
