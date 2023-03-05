import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)

while True :
    keyvalue = cv2.waitKey()
    if keyvalue == ord('c') or keyvalue == ord('C') :
        img = ~img
        cv2.imshow('image', img)
    elif keyvalue == 27 :
        break

cv2.destroyAllWindows()