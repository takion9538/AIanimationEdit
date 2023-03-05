import sys
import cv2

cap = cv2.VideoCapture('Jellyfish.mp4')

if not cap.isOpened() :
    sys.exit()

print('가로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 갯수 : ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))


