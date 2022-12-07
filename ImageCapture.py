from djitellopy import tello
import cv2 as cv
from time import sleep #this adds the delays in the commands we want...

me = tello.Tello()
me.connect() #connection for tello...
print(me.get_battery())

me.stream_on()

while True:
    img = me.get_frame_read().frame
    img = cv.resize(img, (360, 240)) #the smaller the frame the faster the results...
    cv.imshow("Window for Image Capture", img)
    cv.waitKey(0)