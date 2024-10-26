import cv2 as cv
import numpy as np 

if __name__ == "__main__":
    image_path = '/home/avivi/Pictures/img3.jpeg'

    # Draw blank
    blank = np.zeros((500, 500, 3), dtype='uint8')
    blank[:, :] = 200,255,20
    # Draw filled rectangle, circle, line
    cv.rectangle(blank, (0,0), (blank.shape[1]//4, blank.shape[0]//2), color=(0,0,255), thickness=2)

    center_circle = (blank.shape[1]//4, blank.shape[0]//4)
    cv.circle(blank, center=center_circle, radius=40, color=(100, 100, 0), thickness=3)

    cv.line(blank, pt1=center_circle, pt2=(center_circle[0]+100, center_circle[1]+200), color=(200, 55, 76), thickness=4)

    # write Text
    cv.putText(blank, text='hello there', org=(300, 50), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(10,10,10), thickness=2)

    cv.imshow('Blank', blank)


    #img = cv.imread(image_path)
    #cv.imshow('Img', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

