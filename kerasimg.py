from keras.preprocessing import image
from matplotlib import pyplot as plt
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
img = image.load_img('om.jpeg', target_size=(1080, 1080,3))
x = image.img_to_array(img)
plt.imshow(img)
plt.show()
heatmap = np.mean(x,axis = -1)
heatmap = np.maximum(heatmap,100)

plt.matshow(heatmap)
plt.show()

