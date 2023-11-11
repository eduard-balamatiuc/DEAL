import cv2
import numpy as np
import os  
from fastiecm_map import fastiecm 




original = cv2.imread(f'{os.getcwd()}/test.jpg') # load image 

def run_ndvi(image):
    image = rgb_to_bgr(image)
    contrasted = contrast_stretch(image)
    ndvi = calc_ndvi(contrasted)
    ndvi_contrasted = contrast_stretch(ndvi)
    color_mapped_prep = ndvi_contrasted.astype(np.uint8) 
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    cv2.imwrite('ndvi_colored.png', color_mapped_image) 


def rgb_to_bgr(rgb_img):
    image_bgr = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    return image_bgr

def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    return out  


def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi





run_ndvi(original)