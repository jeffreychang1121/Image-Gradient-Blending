
import cv2
import numpy as np
import matplotlib.pyplot as plt
from maskImage import maskImage
from seamlessCloningPoisson import seamlessCloningPoisson

# parameter
offsetX = 10
offsetY = 10
shape = (150,200)

# read image
target = cv2.imread('TargetImage.png')
target = target[:,:,::-1]
# print(target.dtype)
print(target.shape)
source = cv2.imread('SourceImage.png')
source = source[:,:,::-1]
# print(source.dtype)
print(source.shape)

# resize image
source = cv2.resize(source, shape, interpolation=cv2.INTER_CUBIC)

# create mask
mask = maskImage(target)

# save mask
# np.save('goddess.npy', mask);

# load mask
mask = np.load('mask_2.npy')

# run blending
resultImg = seamlessCloningPoisson(source, target, mask, offsetX, offsetY)
print(resultImg.shape)

# show image
plt.imshow(np.uint8(resultImg))
plt.show()