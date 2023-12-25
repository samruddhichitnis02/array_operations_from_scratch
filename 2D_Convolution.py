import cv2
import numpy as np

# referred from -> https://www.youtube.com/watch?v=p6tG-dep8f4&t=325s
# This convolution is done on gray images
# This performs the 2D convolution on images
# Below are the steps to perform the convolution
# Step 1. Calculate the target size for the convolved image
# Step 2. Write the convolve function 


# Step 1: Calculating the target size
def calculate_target_size(img, kernel, padding, stride):
    # There is a formula which tells what would be the output shape of the image when we give
    # it the original image shape, kernel size/convolution matrix size, padding and stide information
    # the formula is (W - K + 2P / S ) + 1
    # W -> Image Size
    # K -> Kernel Size or Convolution Image Size
    # P - > Padding
    # S -> Stride
    # here the image shape should be even that is a square shaped image

    # Here we will consider Stride = 1 and Padding = 0 for simplicity and kernel size = 3
    W = img.shape[0]
    Ot_shape = ((W - kernel + (2 * padding)) / stride) + 1
    return Ot_shape

# Step 2: Write Function for convolution
def convolve(img):
    k = 3

    # get the target size from calculate_target_size function
    target_size = int(calculate_target_size(img, kernel = k, padding = 0, stride = 1))
    print(target_size)

    # create another array which can hold the resulting convolutions
    convolved_img = np.zeros([target_size, target_size])

    # sobel filter
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    for i in range(target_size):
        for j in range(target_size):
            mat = img[i : i + k, j : j + k]
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
    
    return convolved_img

if __name__ == '__main__':
    # reading a color image using cv2
    img = cv2.imread('dog.jpg')

    # converting the color image to gray scale image so as to pass it to convolve function
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # reshaping the image to get even shape
    resized_image = cv2.resize(gray_img, (gray_img.shape[0], gray_img.shape[0])) 

    convolved_image = convolve(resized_image)