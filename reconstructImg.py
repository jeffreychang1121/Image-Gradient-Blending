'''
  File name: reconstructImg.py
  Author:
  Date created:
'''
import numpy as np

def reconstructImg(indexes, red, green, blue, targetImg):
    # range value between 0,255
    red = np.clip(red,0,255)
    green = np.clip(green,0,255)
    blue = np.clip(blue, 0,255)

    # coordinate of the matrix where is nonzero
    [row, col] = np.where(indexes > 0)

    # replace with the result
    targetImg[row, col, 0] = red[:]
    targetImg[row, col, 1] = green[:]
    targetImg[row, col, 2] = blue[:]
    resultImg = targetImg

    return resultImg