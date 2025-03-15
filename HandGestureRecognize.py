from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import pickle
import os
import imutils

main = tkinter.Tk()
main.title("Create Gesture")
main.geometry("1300x1200")

global filename
global classifier

bg = None
global name


bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)



def remove_background(frame):
    fgmask = bgModel.apply(frame, learningRate=0)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

def uploadDataset():
    global name
    name = simpledialog.askstring("Enter Gesture Name to save images", "Enter Gesture Name to save images", parent=main)
    if os.path.exists("Dataset/"+name) == False:
        os.mkdir("Dataset/"+name)


def run_avg(image, aWeight):
    global bg
    if bg is None:
        bg = image.copy().astype("float")
        return
    cv2.accumulateWeighted(image, bg, aWeight)

def segment(image, threshold=25):
    global bg
    diff = cv2.absdiff(bg.astype("uint8"), image)
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
    ( cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        return
    else:
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)


def webcamPredict():
    global name
    count = 0
    fgbg2 = cv2.createBackgroundSubtractorKNN(); 
    aWeight = 0.5
    camera = cv2.VideoCapture(0)
    top, right, bottom, left = 10, 350, 325, 690
    num_frames = 0
    while(True):
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=700)
        frame = cv2.flip(frame, 1)
        clone = frame.copy()
        (height, width) = frame.shape[:2]
        roi = frame[top:bottom, right:left]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (41, 41), 0)
        if num_frames < 30:
            run_avg(gray, aWeight)
        else:
            temp = gray
            hand = segment(gray)
            if hand is not None:
                (thresholded, segmented) = hand
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                roi = frame[top:bottom, right:left]
                roi = fgbg2.apply(roi); 
                cv2.imwrite("test.jpg",roi)
                cv2.imwrite("Dataset/"+name+"/"+str(count)+".png",roi)
                count = count + 1
                print(count)
                if count > 500:
                    break
                cv2.imshow("video frame", roi)
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)
        num_frames += 1
        cv2.imshow("Video Feed", clone)
        keypress = cv2.waitKey(1) & 0xFF
        if keypress == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()    
    

    
    
font = ('times', 16, 'bold')
title = Label(main, text='Create Gesture',anchor=W, justify=CENTER)
title.config(bg='yellow4', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)


font1 = ('times', 13, 'bold')
upload = Button(main, text="Enter Gesture name to save images", command=uploadDataset)
upload.place(x=50,y=100)
upload.config(font=font1)  


predictButton = Button(main, text="Start Webcam", command=webcamPredict)
predictButton.place(x=50,y=250)
predictButton.config(font=font1)



main.config(bg='magenta3')
main.mainloop()
