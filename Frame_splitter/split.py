#python split.py
from imutils.video import VideoStream
from imutils.video import FPS
import time
import cv2
import numpy as np
import os

# Playing video from camera:
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
#cap = cv2.VideoCapture('C:\\Users\saagr\Videos\gagan annual day 2019\sample_vid.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

fps = FPS().start()
currentFrame = 0
while(True):
    # Capture frame-by-frame
    frame = vs.read()
    #ret, frame = cap.read()
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1
    fps.update()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
     break

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()    
# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()