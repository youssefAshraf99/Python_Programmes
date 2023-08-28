# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:32:31 2021

@author: pc
"""
import cv2
import numpy as np

eye = cv2.CascadeClassifier('haarcascade_eye.xml')
face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

Kernal = np.ones((3, 3), np.uint8)      #Declare kernal for morphology

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)        ##Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

ret, frame = cap.read()                     ##Read image frame
frame = cv2.flip(frame, +1)                     ##Flip the image in case your camera capures inverted images
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      ##Convert image to grayscale

detect_face = face.detectMultiScale(gray, 1.2, 1)   ##Detect Face