import sys
import cv2
import numpy as np

cap = cv2.VideoCapture('Jellyfish.mp4')
cap2 = cv2.VideoCapture('Rose.mp4')

if not cap.isOpened() :
    sys.exit()

print('프레임1 갯수 : ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print('프레임2 갯수 : ', int(cap2.get(cv2.CAP_PROP_FRAME_COUNT)))

frame_cnt1 = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS : ', fps)
effect_frames = int(fps * 2)

delay = round(1000 / fps)
print('delay : ', delay)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('effect.avi', fourcc, fps, (w, h))

for i in range(frame_cnt1 - effect_frames) :
    ret1, frame1 = cap.read()

    if not ret1 :
        print('프레임을 읽을 수 없습니다.')
        sys.exit()

    out.write(frame1)

    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

for i in range(effect_frames, frame_cnt2) :
    ret2, frame2 = cap2.read()

    if not ret2 :
        print('프레임을 읽을 수 없습니다.')
        sys.exit()

    out.write(frame2)

    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

for i in range(effect_frames) :
    ret1, frame1 = cap.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2 :
        print('프레임을 읽울 수 없습니다.')
        sys.exit()

    dx = int(w / effect_frames) * i

    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    out.write(frame)
    cv2.imshow('output', frame)
    cv2.waitKey(delay)

cap.release()
cap2.release()
out.release()
cv2.destroyAllWindows()