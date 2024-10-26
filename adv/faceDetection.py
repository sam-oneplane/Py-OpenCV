import cv2 as cv
import numpy as np

def haarCascade(img: cv.typing.MatLike, xml_path: str)-> int:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(xml_path) # 'haar_cascade.xml'
    face_rect = haar_cascade.detectMultiScale(image=gray,
                                              scaleFactor=1.05,
                                              minNeighbors=2)
    for (x,y,w,h) in face_rect:
        cv.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255), thickness=2)
    
    return len(face_rect)

    

if __name__ == "__main__":

    image_path = '/home/avivi/Pictures/nz22.jpg'

    img = cv.imread(image_path)
    scale = 0.95
    resize =  cv.resize(img, 
                        dsize=(int(img.shape[1] * scale), int(img.shape[0] * scale)),
                        interpolation=cv.INTER_AREA)
    
    xml_path = '/home/avivi/Developer/Python/OpenCV/adv/haar_face.xml'
    '''
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(xml_path) # 'haar_cascade.xml'
    face_rect = haar_cascade.detectMultiScale(image=gray,
                                              scaleFactor=1.05,
                                              minNeighbors=4)
    S: str = f'number of faces detacted: {len(face_rect)}'
    print(S)
    '''
    faces =  haarCascade(img, xml_path)
    print (f'number of faces detacted: {faces}')
    
    cv.imshow('Face Detction', img)
    cv.waitKey(0)
    cv.destroyAllWindows()