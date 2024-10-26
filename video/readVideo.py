import cv2 as cv
import os
import matplotlib.pyplot as plt

video_path = os.path.join('/','home', 'avivi', 'Videos', 'video20190613.mp4')

# Capture video
capture = cv.VideoCapture(video_path) # 0,1,2,3.. int is for live web cammera

# Capture Properties
hight = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
fps = capture.get(cv.CAP_PROP_FPS)

videoWriter = cv.VideoWriter(os.path.join('/','home', 'avivi', 'Videos', 'videoLibby.avi'),
                             fourcc=cv.VideoWriter.fourcc(c1='P', c2='I', c3='M', c4='1'),
                             fps=fps,
                             frameSize=(width, hight))

print(hight, width)
print(f'Video frames: {capture.get(cv.CAP_PROP_FRAME_COUNT)} with  {fps} a second')

# Rander Video
scale = 0.20
for _ in range(int(capture.get(cv.CAP_PROP_FRAME_COUNT))):
    isTrue, frame = capture.read()
    if isTrue:
        hsv = cv.cvtColor(frame, code=cv.COLOR_BGR2HSV)
        videoWriter.write(hsv)

        rescale = cv.resize(hsv, 
                            dsize=(int(frame.shape[1] * scale), int(frame.shape[0] * scale)),
                            interpolation=cv.INTER_CUBIC)
        
        cv.imshow('RescaleVideo', rescale)

    if cv.waitKey(10) & 0xFF == ord('q'):
        plt.imshow(cv.cvtColor(hsv, cv.COLOR_BGR2RGB))
        break
    
videoWriter.release()
capture.release() # release the pointer
cv.destroyAllWindows()

plt.show()
