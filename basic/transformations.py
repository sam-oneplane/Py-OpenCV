import cv2 as cv
import numpy as np
import basic_func as bf 



def show_img(img, label: str):
    cv.imshow(label, img)

# Translation
'''
    -x --> left
    x --> right
    -y --> up
    y --> down
'''

def translate(img: cv.typing.MatLike, x: int, y: int) -> cv.typing.MatLike:
    transMatrix = np.float64([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)


# Rotation 
def rotate(img: cv.typing.MatLike, angle, rotPoint=None) -> cv.typing.MatLike:
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, (width, height))

# Flip
def flip(img: cv.typing.MatLike, code: int) -> cv.typing.MatLike:
    return cv.flip(img, code) # 0 , 1, or -1 




if __name__ == "__main__":
    image_path = '/home/avivi/Pictures/traffic_sign.jpg'

    img = cv.imread(image_path)
    resize = bf.resizeFrame(img, 0.4)
    show_img(resize, "basic image")

    translated = translate(resize, 100, 150)
    show_img(translated, "translated image")

    rotation_point = (resize.shape[1]//4, resize.shape[0]//4)
    rotation = rotate(resize, 15, rotation_point)
    show_img(rotation , "rotated image")
    
    cv.waitKey(0)