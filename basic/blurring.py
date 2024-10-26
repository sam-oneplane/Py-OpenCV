import cv2 as cv
import numpy as np
import basic_func as bf


# bluring
def gaussingBlur(img: cv.typing.MatLike, kernelSize: tuple, sdX: float) -> cv.typing.MatLike:
    return cv.GaussianBlur(img, ksize=kernelSize, sigmaX=sdX , borderType=cv.BORDER_DEFAULT)

if __name__ == "__main__":
    image_path = '/home/avivi/Pictures/avibby5.jpeg'

    img = cv.imread(image_path)
    resize = bf.resizeFrame(img, 0.75)

    # blur by avg kernel values:
    kernelAvgBlur = cv.blur(resize, ksize=(7,7))
    # gaussian blur
    gaussBlur = gaussingBlur(resize, (7,7), 0)
    # median blur 
    medianBlur = cv.medianBlur(resize, ksize=7)
    # bilateral
    billateral = cv.bilateralFilter(resize, d=10, sigmaColor=30, sigmaSpace=30)


    cv.imshow("kernel average blur", kernelAvgBlur)
    cv.imshow("kernel gaussian blur", gaussBlur)
    cv.imshow("kernel median blur", medianBlur)
    cv.imshow("kernel bilateral blur", billateral)

    cv.waitKey(0)
    cv.destroyAllWindows()
    