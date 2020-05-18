from scipy import signal
from skimage import io, feature
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


def crop_image(img):
    crop_img = img[0:img.shape[0], 50:img.shape[1]]
    return crop_img

def normalize(img):
    min_pixel = np.amin(img)
    max_pixel = np.amax(img)
    norm_img = img - min_pixel * 1 / (max_pixel - min_pixel)
    return norm_img




#It doesn't work perfectly yet, each picture has slightly different brightness parameters.
def brightPoints(image):
    img = cv.imread(image) 
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
    h, s, v = cv.split(hsv) 
    limit = v.max () 

    hsv_min = np.array((0, 0, 180), np.uint8) 
    hsv_max = np.array((225, 225, limit), np.uint8)

    img1 = cv.inRange(hsv, hsv_min, hsv_max) 

    moments = cv.moments(img1, 1) 

    x_moment = moments['m01']
    y_moment = moments['m00']

    area = moments['m00']

    x = int(x_moment / area) 
    y = int(y_moment / area) 
    
    points = cv.imwrite("points.jpg" , img1)
    
    return points


def normalize2(img):
    
    """
    normalisation function with an added part to resize image to 257 grey values
    """
    
    min_pixel = np.amin(img)
    max_pixel = np.amax(img)
    norm_img = img - min_pixel * 1 / (max_pixel - min_pixel)
    norm2 = norm_img/(max_pixel/257)
    return norm2


def circle_convolution(image, radius, kernelsize):
    """
    function to convolve img with a kernel containing a circle filter
    kernelsize= size of kernel
    radius= radius of circle
    """
    
    arr = np.zeros((kernelsize, kernelsize))
    arr[:,:] = -100
    rr, cc = draw.circle(kernelsize/2, kernelsize/2, radius=radius, shape=arr.shape)
    arr[rr, cc] = 1000
    
    conv = signal.convolve2d(img_after, arr, mode='same')
    return conv


def thresholding(image, thres):
    """
    function for thresholding
    """
    binary_img=np.where(norm_electrode>thres, 200, 0)
    return binary_img
