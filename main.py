import cv2

image = cv2.imread('fruits.jpg')
cv2.imshow('origianl', image)

cv2.waitKey(0)
cv2.destroyAllWindows()