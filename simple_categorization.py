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

image_location = 'img/white.png' # 'img/black.png'
# Open and convert to grayscale
img = Image.open(image_location).convert('L')
# Convert to numpy array
img_arr = np.array(img, np.uint8)
category = singlepixel_categorizer(img_arr)
print(f'category: {category}')
