import cv2 as cv
import numpy as np
import os

DIR = r'/home/avivi/Developer/Python/OpenCV/adv/resources/Faces/train'
XML = r'/home/avivi/Developer/Python/OpenCV/adv/haar_face.xml'

'''
    collect bounding boxes and index for each person's folder
'''
def collect(features: list, labels: list, people: list):

    haar_cascade = cv.CascadeClassifier(filename=XML) 
    for person in people:
        path = os.path.join(DIR, person)
        # collect label
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)

            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(image=gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


def train(features: list, labels: list):
    face_recognizer = cv.face.LBPHFaceRecognizer.create()
    features = np.array(features, dtype='object')
    labels = np.array(labels)
    face_recognizer.train(features, labels)
    face_recognizer.save('adv/face_trained.yml')
    np.save('adv/features.npy', features)
    np.save('adv/labels.npy', labels)



if __name__ == "__main__":

    people = []
    for d in os.listdir(DIR):
        people.append(d)
    
    features= []
    labels = []

    print(f'people list {people}')
    collect(features, labels, people)
    print(f'labels list len {len(labels)}')
    print(f'features list len {len(features)}')

    train(features, labels)
    print('Done training-------------------')

