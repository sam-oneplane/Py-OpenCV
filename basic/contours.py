import cv2 as cv
import numpy as np
import basic_func as bf



def imgContours(img: cv.typing.MatLike) -> tuple:
    contours, _ = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    return contours

def imgThreshold(img: cv.typing.MatLike, thresh: int, maxval: int) -> tuple:
    rt, thresh = cv.threshold(img, thresh, maxval, cv.THRESH_BINARY)
    return (rt, thresh)


def drawContours(contours, blank):
    cv.drawContours(blank, contours, contourIdx=-1, color=(255,0,0), thickness=1)
    return blank

if __name__ == "__main__":
    image_path = '/home/avivi/Pictures/avivi1.jpeg'

    img = cv.imread(image_path)
    resize = bf.resizeFrame(img, 0.4)
    gray = bf.converToGrayScale(resize)
    rt, thresh = imgThreshold(gray, 125, 255)

    blur = bf.gaussingBlur(gray)
    canny = bf.cannyEdgeDetection(blur, 100, 2)
    '''
    for contours we can use 
        1. canny edge detection after bluring
        2. binary (or other) threshold on image 
    '''
    contours = imgContours(thresh)
    contours1 = imgContours(canny)
    # Draw contours
    blank = np.zeros(gray.shape, dtype='uint8')
    drawContours(contours, blank)

    blank1 = np.zeros(gray.shape, dtype='uint8')
    drawContours(contours1, blank1)

    cv.imshow('image', resize)
    cv.imshow('blur', blur)
    cv.imshow('drawnContours', blank)
    cv.imshow('drawnContours using canny', blank1)
    print(f'{len(contours)} thd contours found in {gray.shape}')
    print(f'{len(contours1)} canny contours found in {gray.shape}')
    
    cv.waitKey(0)