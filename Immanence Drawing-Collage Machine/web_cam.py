#importing required libraries
import cv2
import numpy as np
import os

def save_frame():
    # taking the input from webcam
    vid = cv2.VideoCapture(0)
    # capturing the current frame
    _, frame = vid.read()
    # saving the current frame
    cv2.imwrite( 'SaveTest.jpg' , frame)
    #delete file
    os.remove('SaveTestRenamed.gif')
    #rename file as gif
    os.rename('SaveTest.jpg' , 'SaveTestRenamed.gif')

save_frame()
