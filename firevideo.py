# code for running YOLOv8n model for fire detection

from ultralytics import YOLO
import cv2
import cvzone
import math
import os
import sys
import glob

if len(sys.argv)==1:
    print("please enter the filename")
    sys.exit(0)

# read the coco class labels
classnames = ['fire']

show_gray = False

model = YOLO("fire.pt")  # custom model

##cap = cv2.VideoCapture(0) # 1 for multiple cameras

video_in = sys.argv[1]
#cap = cv2.VideoCapture('fire4.mp4')
cap = cv2.VideoCapture(video_in)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if show_gray:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("BiaTech Video Processing", gray_frame)
    else:

        # call the model here
        result = model(frame,stream=True)

        # Getting bbox,confidence and class names informations to work with
        for info in result:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                oclass = int(box.cls[0])
                if confidence > 55:
                    x1,y1,x2,y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,255),2)
                    cvzone.putTextRect(frame, f'{classnames[oclass]} {confidence}%', [x1 + 10, y1 +100], scale=1.5,thickness=2)


        cv2.imshow("BiaTech Video Processing", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

