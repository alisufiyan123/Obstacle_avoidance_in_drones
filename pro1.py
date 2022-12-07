import cv2 as cv
import numpy as np

#see the thresh.py file and work with the functions to get the best possible thresholded photos...

#Reading original image
img_main = cv.imread("Photos/desk.jpg")
cv.imshow("Original Version", img_main)

#Resizing the main image because we dont need such a large frame
img = cv.resize(img_main, (420, 420), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Version", gray)

#blurring image for making the objects stand out from the overall image..
blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur Version", blur)

#conversion to Canny Edge for detecting possible edges..
canny = cv.Canny(blur, 45, 95) #please find the best threshold for over all images.
# cv.imshow("Canny Version", canny)

####################DETAILING THE IMAGE FOR CLEAR DETECTION###############
                                        #these are channels incase of multicolor image we will increase channels so all the colors are handled seprately for clearity
clear_canny = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow("Clear Canny Version", clear_canny)

############################################################################
blank = np.zeros((300, 300, 3), dtype='uint8' ) #creating an empty window of 300x300 resolution and the 3 means number of color channels => R G B
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Blank', blank)

#segmentation of Image for selecting the segment with least amount of pixels...
segmented_blank = cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0))
# cv.imshow("Blank Segmented Version", segmented_blank)

#########TESTING############ it failed so we have to find a method to convert and divide the image into segments... and then look for segments with lesser white pixel
# rgb_convert = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# segmented_canny = cv.rectangle(rgb_convert, (0,0), (rgb_convert.shape[1]//2, rgb_convert.shape[0]//2), (0, 255, 0))
segmented_canny = cv.rectangle(clear_canny, (0,0), (clear_canny.shape[1]//2, clear_canny.shape[0]//2), (0, 255, 0))
# cv.imshow("Canny Segmented Version", segmented_canny)


"""
//SUDO CODE
#Motion Control
if (S(2) > 1000 pixel):
    if (S(1) < 500 pixel) and (S(1) <= S(3)):
        Move (left)
    elif (S(3) < 500 pixel) and (S(3) <= S(1)):
        Move (right)
    elif (S(4) < 500 pixel) and (S(4) <= S(5)) and (vehicle High > h):
        Move (down)
else:
    Move (up)
end
"""

"""
############HERE WE ARE TRYING TO MATHEMATICALLY TREAT BY CONVERTING TO RGB FIRST######################
#here we tried this because numpy works with drawing on RGB and originally we had BGR so we tried to convert the BGR2RGB and then working with Segmentation but it needs some refining...
##ITS USELESS##
#reading original image
img_main = cv.imread("Photos/home_test.jpg")
# cv.imshow("Original Version", img)


#Resizing the main image because we dont need such a large frame
img = cv.resize(img_main, (720, 650), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", img)

rgb_converted = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#converting to grayscale
gray = cv.cvtColor(rgb_converted, cv.COLOR_RGB2GRAY)
cv.imshow("Gray Version", gray)

#blurring image for making the objects stand out from the overall image..
blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur Version", blur)

#conversion to Canny Edge for detecting possible edges..
canny = cv.Canny(blur, 45, 95) #please find the best threshold for over all images.
cv.imshow("Canny Version", canny)

####################DETAILING THE IMAGE FOR CLEAR DETECTION###############
                                        #these are channels incase of multi colorimage we will increase channels so all the colors are handled seprately for clearity
clear_canny = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Clear Canny Version", clear_canny)

############################################################################
blank = np.zeros((720, 650, 3), dtype='uint8' ) #creating an empty window of 500x500 resolution and the 3 means number of color channels => R G B
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Blank', blank)


#segmentation Image for selecting the segment with least amount of pixels...
segmented_blank = cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0))
cv.imshow("Blank Segmented Version", segmented_blank)

#########TESTING############
# rgb_convert = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# segmented_canny = cv.rectangle(rgb_convert, (0,0), (rgb_convert.shape[1]//2, rgb_convert.shape[0]//2), (0, 255, 0))
segmented_canny = cv.rectangle(clear_canny, (0,0), (clear_canny.shape[1]//2, clear_canny.shape[0]//2), (0, 255, 0))
cv.imshow("Canny Segmented Version", segmented_canny)
"""

cv.waitKey(0)