import cv2 as cv
import os


DIR = r'/home/avivi/Developer/Python/OpenCV/adv/resources/Faces/train'
XML = r'/home/avivi/Developer/Python/OpenCV/adv/haar_face.xml'
recognizer_path =  r'/home/avivi/Developer/Python/OpenCV/adv/face_trained.yml'

def testRecognizer(recognizer_path: str, img: cv.typing.MatLike, people: list):
    face_recognizer = cv.face.LBPHFaceRecognizer.create()
    face_recognizer.read(recognizer_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(filename=XML)
    faces_rect = haar_cascade.detectMultiScale(image=gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5)
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)

        print(f'Label = {people[label]} with a confidence of {confidence}')
        cv.putText(img, 
                   text=str(people[label]), 
                   org=(20,20), 
                   fontFace=cv.FONT_HERSHEY_COMPLEX, 
                   fontScale=1.0, 
                   color=(0,255,0), 
                   thickness=2)
        cv.rectangle(img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)


if __name__ == "__main__":
    people = []
    for d in os.listdir(DIR):
        people.append(d)

    
    img_path = r'/home/avivi/Developer/Python/OpenCV/adv/resources/Faces/val/jerry_seinfeld/3.jpg'
    img = cv.imread(filename=img_path)
    testRecognizer(recognizer_path, img, people)
    cv.imshow("Image Recognizer", img)

    cv.waitKey(0)
