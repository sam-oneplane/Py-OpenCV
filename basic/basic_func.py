import cv2 as cv
from cv2 import Mat
import numpy as np

# resize Image
def resizeFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    hight = int(frame.shape[0] * scale)
    # to inlarge the image use : interpolation=cv.INTER_CUBIC
    return cv.resize(frame, (width, hight), interpolation=cv.INTER_AREA)

#  Only work for live video
def changeResolution(capture, width, hight):
    
    capture.set(3, width)
    capture.set(4, hight)
    return capture


# Crop image
def cropImag(img: cv.typing.MatLike, st_point_width: int, st_point_hight: int, delta: int) -> cv.typing.MatLike:
    en_point_width = min(img.shape[1], st_point_width+delta)
    en_point_hight = min(img.shape[0], st_point_hight+delta)
    return img[st_point_width:en_point_width, st_point_hight:en_point_hight] 

# convert to grayScale
def converToGrayScale(img: cv.typing.MatLike) -> cv.typing.MatLike:
    '''
    cv.COLOR_BGR2HSV
    cv.COLOR_BGR2LAB
    cv.COLOR_BGR2RGB
    and the revese way
    '''
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# bluring
def gaussingBlur(img: cv.typing.MatLike) -> cv.typing.MatLike:
    return cv.GaussianBlur(img, ksize=(5,5),sigmaX=0 , borderType=cv.BORDER_DEFAULT)

# Edge detection
def cannyEdgeDetection(img: cv.typing.MatLike, low_thd: float, ratio: int) -> cv.typing.MatLike:
    return cv.Canny(img, threshold1=low_thd, threshold2=low_thd*ratio)


# Dialate (on edge detection)
def dilatedEdge(img: cv.typing.MatLike, kernel: tuple, iter: int) -> cv.typing.MatLike:
    dialated_img = cv.dilate(img, kernel=kernel, iterations=iter)
    return cv.erode(dialated_img, kernel=kernel, iterations=iter)

