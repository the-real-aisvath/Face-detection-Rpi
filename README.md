# Face-detection-Rpi
Repository containing the code for my raspberry pi based project to detect faces ,capture the images and mail them automatically 

# Aim of the project 
To create an automatic photo booth that clicks a certain amount of pictures once a face is detected, and emails these pictures to the users making the entire process automatic and contactless at every point

# Use case of the project 
At parties or social gatherings , to click pictures 
to get a nostalgic feeling of the retro photo booth , but modified to today's technology

# Process explanation 
The user walks into the photo booth and visits the web page served by the raspberry pi. Once he enters his details specifying the number of snaps and his email id , The program in Raspberry pi starts working. Once the photos have been snapped, they are automatically mailed to him as he walks out.

# Technical description
A Raspberry pi that runs as a Flask App server. This serves a simple web page that gets the user details regarding the number of snaps the user would like to take and the email id of the user so that the clicked pictures can be mailed to him.
Once the user clicks the submit button, The backend process begins. 

The raspberry pi runs a simple python code that clicks a picture evry five seconds to check if a face is detected. If a face has been detected , the user is prompted that the photo clicking would begin in 3... 2 ... 1.. (in the form of an audio)
After evry snp has been clicked , a clicking sound is played to let the user know that one image has been clicked.

After all the images have been clicked, The user recieves a confirmation in the form of a voice note

The images get mailed to himautomtically through a python code using the smtp mail server.
Thus , the entire process has been modernised and made contactless at the same time.
