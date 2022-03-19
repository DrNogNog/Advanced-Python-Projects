# adaptive thresholding to easily read text
import cv2 as cv

img = cv.imread('bookpage.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #cvt = convert

#thresholding
#grayscale image is a collection of pixels, 0-255 of shades of gray, pivot 50, every value above 50 convert to black and below 50 to white
_, result = cv.threshold(img, 35, 255, cv.THRESH_BINARY)
# we need a higher threshold for top image, and lower for bottom image due to shadows.
adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4) 

#can change 4 variable to edit background noise. 
#81 is an odd to look at neighboring pixels 

cv.imshow('Image', img)
cv.imshow('Result', result)
cv.imshow('Adaptive Result', adaptive)

cv.waitKey(0)
cv.destroyAllWindows()

