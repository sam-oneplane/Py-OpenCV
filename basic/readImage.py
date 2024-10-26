import cv2 as cv
import basic_func as basic_func

image_path = '/home/avivi/Pictures/img1.jpeg'

img = cv.imread(image_path)

rescale_img = basic_func.resizeFrame(img, 0.5)
grayScale_img = basic_func.converToGrayScale(rescale_img)
gaussianBlur_img = basic_func.gaussingBlur(rescale_img)
canny_img = basic_func.cannyEdgeDetection(gaussianBlur_img, 100, 2)
dilated_img = basic_func.dilatedEdge(canny_img, (7,7), 5)
croped_img = basic_func.cropImag(rescale_img, rescale_img.shape[1]//2, rescale_img.shape[0]//2, 300)

cv.imshow('Img', rescale_img)
cv.imshow('BlurImg', gaussianBlur_img)
cv.imshow('CannyImg', canny_img)
cv.imshow('DialatedImg', dilated_img)
cv.imshow('CropedImg', croped_img)


cv.waitKey(0) # wait infinite time


