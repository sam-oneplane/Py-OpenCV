import cv2 as cv
import numpy as np

DIR = '/home/avivi/Developer/Python/OpenCV/adv/resources/Images'
IMAGE = 'woldosBeach.jpg'
WOLDO = 'Waldo.jpeg'

if __name__ == "__main__":

    img = cv.imread(f'{DIR}/{IMAGE}')
    waldo = cv.imread(f'{DIR}/{WOLDO}', 0)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    result = cv.matchTemplate(gray, waldo, method=cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(max_loc)

    cv.circle(img, center=max_loc, radius=20, color=(0,0,255), thickness=3)

    cv.imshow('Beach', img)
    cv.imshow('Woldo', waldo)

    cv.waitKey(0)
    cv.destroyAllWindows()