# code for face detection 
import io
from email_sample import *
import picamera
import cv2
import numpy
import warnings
import pygame
from os import system
from time import sleep
warnings.simplefilter("ignore", DeprecationWarning)
pygame.init()
ch=1
gif=0
def run_camera_recog(ch,gif):                                                           # function for face detection 
    warnings.simplefilter("ignore", DeprecationWarning)
    while(True):
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.resolution = (1080, 720)                                             # capturing the first image every five seconds
            camera.capture(stream, format='jpeg')
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
        image = cv2.imdecode(buff, 1)
        face_cascade = cv2.CascadeClassifier('/home/pi/faces.xml')
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)                         # applying cascade classifiers for identifying a face
        cv2.imwrite('result.jpg',image)
        if(len(faces)>=1):
            if(ch==1):
                i=0                                                                   # capturing 3images
                pygame.mixer.music.load("here_we_go.mp3")
                pygame.mixer.music.play()
                sleep(5)
                with picamera.PiCamera() as camera:
                    for i in range(3):
                        camera.capture('image_set_1_{0:04d}.jpg'.format(i))
                        pygame.mixer.music.load("camsound1.mp3")
                        pygame.mixer.music.play()
                        sleep(2)
                    pygame.mixer.music.load("thankyou.mp3")
                    pygame.mixer.music.play()
                    sleep(3)
                if(gif==1):
                    system('convert -delay 15 -loop 0 image_set_1_*.jpg gif_set_1.gif')
                break
            elif(ch==2):
                i=0
                pygame.mixer.music.load("here_we_go.mp3")
                pygame.mixer.music.play()
                sleep(5)
                with picamera.PiCamera() as camera:                                         # capturing 5 images
                    for i in range(5):
                        camera.capture('image_set_2_{0:04d}.jpg'.format(i))
                        pygame.mixer.music.load("camsound1.mp3")
                        pygame.mixer.music.play()
                        sleep(2)
                    pygame.mixer.music.load("thankyou.mp3")
                    pygame.mixer.music.play()
                    sleep(3)
                if(gif==1):
                    system('convert -delay 15 -loop 0 image_set_2_*.jpg gif_set_2.gif')
                break
            elif(ch==3):
                i=0
                pygame.mixer.music.load("here_we_go.mp3")
                pygame.mixer.music.play()
                sleep(5)                                                            # capturing 10 images
                with picamera.PiCamera() as camera:
                    for i in range(10):
                        camera.capture('image_set_3_{0:04d}.jpg'.format(i))
                        pygame.mixer.music.load("camsound1.mp3")
                        pygame.mixer.music.play()
                        sleep(2)
                    pygame.mixer.music.load("thankyou.mp3")
                    pygame.mixer.music.play()
                    sleep(3)
                if(gif==1):
                    system('convert -delay 15 -loop 0 image_set_3_*.jpg gif_set_3.gif')
                break
        #else:
            #print("no faces detected")
            
        #print("all pictures taken")
        sleep(5)

#run_camera_recog(2,1)

