import cv2 as cv
import numpy as np
import basic_func as bf


if __name__ == "__main__":
    image_path = '/home/avivi/Pictures/avibby1.jpeg'

    img = cv.imread(image_path)
    resize = bf.resizeFrame(img, 0.75)

    B, G, R = cv.split(resize)


    merged = cv.merge([B, G, R])

    blank = np.zeros(resize.shape[0:2], dtype="uint8")
    blue = cv.merge([B, blank, blank]) # only Blue component is active in BGR
    red = cv.merge([blank, blank, R])

    cv.imshow("image", resize)
    cv.imshow("merged", merged)
    cv.imshow("blue", blue)
    cv.imshow("red", red)


    cv.waitKey(0) 

