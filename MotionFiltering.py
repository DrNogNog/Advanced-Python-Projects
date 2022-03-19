import cv2 as cv

video = cv.VideoCapture(0) #real time Camera
#video = cv.VideoCapture('people.mp4') #camera data
subtractor = cv.createBackgroundSubtractorMOG2(300, 50) 
# change 20 and 50 to see if you're getting better results, object is very complicated in actuality. 

#endless loop for frame-by-frame analysis

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply()
        #apply subtractor object we just defined
        cv.imshow('Mask',mask)
        
        if cv.waitKey(5) == ord('X'):
            break
# this is if you don't have a return for a recording (not needed for real time camera data)    
    #else:
        #video = cv.VideoCpature('people.mp4')

cv.destroyAllWindows()
video.release()

    