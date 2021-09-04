import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from MD1 import detection
from s33 import s3_upload

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
is_record = False
while capture.isOpened():
    ret, frame = capture.read()
    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    frame = np.array(frame)
    is_detection=detection(capture)
    if is_record == False and is_detection:
        is_record = True
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        nowDatetime_path = now.strftime('%Y_%m_%d %H_%M_%S')
        video = cv2.VideoWriter(nowDatetime_path +".mp4", fourcc, 15, (frame.shape[1], frame.shape[0]))
    elif is_record == True and not is_detection:
        is_record = False
        video.release()
        s3_upload(nowDatetime_path)
    if is_record == True:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0,0,255), thickness=-1)
    cv2.imshow("output", frame)
capture.release()
cv2.destroyAllWindows()
