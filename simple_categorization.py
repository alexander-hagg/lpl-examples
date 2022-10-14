from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def singlepixel_categorizer(pixel):
    category_labels = ['dunkel', 'hell']
    # Convert to numpy array
    pixel_array = np.asarray(pixel)
    # Categorize grayscale pixel
    if pixel_array[0][0] > 0.5:
        category = 1
    else:
        category = 0
    return category_labels[category]

def image_categorizer(img):
    pass

image_location = 'img/white.png'
# Open and convert to grayscale
img = Image.open(image_location).convert('L')
category = singlepixel_categorizer(img)
print(f'category: {category}')

image_location = 'img/black.png'
img = Image.open(image_location).convert('L')
category = singlepixel_categorizer(img)
print(f'category: {category}')

# plt.imshow(img)
# plt.show()
# img = Image.open('img/white.png')
