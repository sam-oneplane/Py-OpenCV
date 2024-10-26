import cv2 as cv
import numpy as np

def laplacian(img: cv.typing.MatLike) -> cv.typing.MatLike:
    lap = cv.Laplacian(img, ddepth=cv.CV_64F)
    return np.uint8(np.absolute(lap))

def sobel(img: cv.typing.MatLike) -> cv.typing.MatLike:
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
    return cv.bitwise_or(sobelx, sobely)

def canny(img: cv.typing.MatLike, low_thd: float, high_thd: float) -> cv.typing.MatLike:
    return cv.Canny(img, threshold1=low_thd, threshold2=high_thd)



if __name__ == "__main__":

    image_path = '/home/avivi/Pictures/nz16.jpg'

    img = cv.imread(image_path)
    scale = 0.95
    resize =  cv.resize(img, 
                        dsize=(int(img.shape[1] * scale), int(img.shape[0] * scale)),
                        interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(resize, code=cv.COLOR_BGR2GRAY)
    cv.imshow('Laplacian edge dsetection', laplacian(gray))
    cv.imshow('Sobel edge dsetection', sobel(gray))
    cv.imshow('Canny edge dsetection', canny(gray, 160, 190))
    cv.waitKey(0)
    cv.destroyAllWindows()