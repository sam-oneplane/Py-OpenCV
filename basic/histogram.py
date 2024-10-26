import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hist_on_gray(img: cv.typing.MatLike) -> tuple:
    gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
    blank = np.zeros((gray.shape), dtype='uint8')
    circle = cv.circle(blank, center=(gray.shape[1]//2-20, gray.shape[0]//2-40), radius=gray.shape[0]//5, color=255, thickness=cv.FILLED)
    masked_img = cv.bitwise_and(gray, gray, mask=circle)
    return masked_img, cv.calcHist([gray], 
                       channels=[0], 
                       mask=masked_img, 
                       histSize=[256], 
                       ranges=[0,256])

def hist_on_image(img: cv.typing.MatLike):
    hist = []
    blank = np.zeros((img.shape[:2]), dtype='uint8')
    mask = cv.circle(blank, center=(img.shape[1]//2-20, img.shape[0]//4), radius=img.shape[0]//5, color=255, thickness=cv.FILLED)
    masked_img = cv.bitwise_and(img, img, mask=mask)
    for i  in range(3):
        hist.append(cv.calcHist([img], 
                    channels=[i], 
                    mask=mask, # mask shold be binary format
                    histSize=[256], 
                    ranges=[0,256]))
    return masked_img, hist


if __name__ == "__main__":

    image_path = '/home/avivi/Pictures/avibby3.jpeg'

    img = cv.imread(image_path)
    scale = 0.6
    resize =  cv.resize(img, 
                        dsize=(int(img.shape[1] * scale), int(img.shape[0] * scale)),
                        interpolation=cv.INTER_AREA)

    colors = ['b', 'g', 'r']
    # masked_img, gray_hist = hist_on_gray(resize)
    masked_img, colored_hist = hist_on_image(resize)


    plt.figure()
    plt.title('Colored Histogram')
    plt.xlabel('GBR Value') 
    plt.ylabel('# Of Pixels')
    for i, hist in enumerate(colored_hist):
        plt.plot(hist, color=colors[i])
        plt.xlim([0, 256])
    plt.show()

    cv.imshow('Masked Image', masked_img)

    cv.waitKey(0)
    cv.destroyAllWindows()