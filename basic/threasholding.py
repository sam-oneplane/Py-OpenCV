import cv2 as cv
import numpy as np

def simple(img: cv.typing.MatLike, thd: float) -> cv.typing.MatLike:
    gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
    _, out = cv.threshold(gray, thresh=thd, maxval=255, type=cv.THRESH_BINARY)
    return out

def adaptive(img: cv.typing.MatLike) -> cv.typing.MatLike:
    gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
    adaptive_thd = cv.adaptiveThreshold(gray, 
                                        maxValue=255, 
                                        adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        thresholdType=cv.THRESH_BINARY, 
                                        blockSize=11, 
                                        C=4)
    return adaptive_thd



if __name__ == "__main__":

    image_path = '/home/avivi/Pictures/avibby3.jpeg'

    img = cv.imread(image_path)
    scale = 0.6
    resize =  cv.resize(img, 
                        dsize=(int(img.shape[1] * scale), int(img.shape[0] * scale)),
                        interpolation=cv.INTER_AREA)
    cv.imshow("Threshold Image", simple(resize, 100))
    cv.imshow("Adaptive Threshold Image", adaptive(resize))
    cv.waitKey(0)
    cv.destroyAllWindows()