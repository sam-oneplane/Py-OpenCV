import cv2 as cv
import os


# Capture web cam
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('error wrong id')
    exit(1)
print('Success-----')

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

def frame_color(frame, color):
    return cv.cvtColor(frame, color)

state = 'n'
idx = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    color = {'n': frame, 
            's': cv.cvtColor(frame, cv.COLOR_BGR2HLS),
            'v': cv.cvtColor(frame, cv.COLOR_BGR2HSV)}
    if ret:
        cv.imshow('RescaleVideo', color[state])

    if cv.waitKey(1) & 0xFF == ord('s'):
        state = 's'
    if cv.waitKey(1) & 0xFF == ord('v'):
        state = 'v'
    if cv.waitKey(1) & 0xFF == ord('n'):
        state = 'n'
    if cv.waitKey(1) & 0xFF == ord('p'):
        path = os.path.join('/','home', 'avivi', 'Pictures', f'samiam_{idx}.jpeg')
        cv.imwrite(path, color[state])
        idx += 1

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() # release the pointer
cv.destroyAllWindows()