import cv2

import time, sys, os
from gpiozero import OutputDevice, Button
from picamera2 import Picamera2

# find user
users  = []
users.append(os.getlogin())

direction_pin = OutputDevice(20)
step_pin = OutputDevice(21)
WaitTime = 0.001

#thres = 0.45 # Threshold to detect object

classNames = []
classFile = "/home/" + users[0] + "/Desktop/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/" + users[0] + "/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/" + users[0] + "/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

                    time.sleep(2)
                    direction_pin.on()
                    for x in range(400):
                        step_pin.on()
                        time.sleep(WaitTime)
                        step_pin.off()
                        time.sleep(WaitTime)

    return img,objectInfo

if __name__ == "__main__":
    # start Pi camera
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

    #Below is the never ending loop that determines what will happen when an object is identified.
    while True:
        # GET AN IMAGE from Pi camera
        img = picam2.capture_array("main")
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        result, objectInfo = getObjects(img,0.70,0.2, objects=['person'])
        #print(objectInfo)

        cv2.imshow("Output",img)
        cv2.waitKey(1)
