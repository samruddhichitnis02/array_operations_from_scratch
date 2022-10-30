import cv2
import numpy as np

cat = cv2.imread('cat.jpeg')

def get_padding(arr):
    return arr // 2

def add_padding_to_img(img, padding_width):
    padded_image = np.zeros(shape = (img.shape[0] + padding_width * 2,  img.shape[1] + padding_width * 2, 3))
    padded_image[padding_width : - padding_width, padding_width : - padding_width, :] = img
    return padded_image

pad_3x3 = get_padding(3)

padded_img = add_padding_to_img(cat, pad_3x3)
print(padded_img)