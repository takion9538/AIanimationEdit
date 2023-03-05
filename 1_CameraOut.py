import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened() :
    print('카메라를 열 수 없습니다.')
    sys.exit()

w = '가로 사이즈 : ', int(cap.get(cv2.CAP_PROT_FRAME_WIDTH))
h = '세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 포맷(코덱)
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened() :
    print('파일을 열 수 없습니다.')
    cap.release()
    sys.exit()

while True :
    ret, frame = cap.read()

    if not ret :
        break

    inversed = ~frame

    out.write(inversed)
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27 :
        break

cap.release()
out.release()
cv2.destroyAllWindows()