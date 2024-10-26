import cv2 as cv
import numpy as np 
import basic_func as bf

if __name__ == "__main__":

    image_path = '/home/avivi/Pictures/avibby5.jpeg'

    img = cv.imread(image_path)
    resize = bf.resizeFrame(img, 0.55)

    ''' REMARK :
    if we use blank as a mask to resize image using bitwise op
    blank and resize image has to be the same frame size
    ''' 
    blank = np.zeros((resize.shape[0:2]), dtype='uint8')

    # draw white rectangle on blank copy 
    rectangle = cv.rectangle(blank.copy(), pt1=(resize.shape[1]//3-140, resize.shape[0]//3-140), pt2=(resize.shape[1]//3+140, resize.shape[0]//3+140), color=255, thickness=cv.FILLED)
    # draw white circle on blank copy
    circle = cv.circle(blank.copy(), center=(resize.shape[1]//3, resize.shape[0]//3), radius=160, color=255, thickness=cv.FILLED)

    bitwise_and = cv.bitwise_and(rectangle, circle)
    bitwise_or = cv.bitwise_or(rectangle, circle)
    bitwise_nxor = cv.bitwise_not(cv.bitwise_xor(rectangle, circle))

    masked_img0 = cv.bitwise_and(resize, resize, mask=bitwise_or)
    masked_img = cv.bitwise_and(resize, resize, mask=circle)

    cv.imshow("Bitwise OR", bitwise_or)
    cv.imshow("Masked image", masked_img)
    cv.imshow("Wired Masked image", masked_img0)

    cv.waitKey(0)
    cv.destroyAllWindows()
