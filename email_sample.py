# contains code for etching the images , attaching them and mailing them to the entered mail id

import smtplib,ssl
#from smtplib import SMPTException
import os
import warnings
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders
warnings.simplefilter("ignore", DeprecationWarning)
def attach_file(filename):
    part = MIMEBase('application', 'octect-stream')
    part.set_payload(open(filename, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s' % os.path.basename(filename))
    return part
  

def send_an_email3(toaddr):# image path setdef send_an_email():
    warnings.simplefilter("ignore", DeprecationWarning)
    
    me = '@gmail.com'          # your id
    subject = "Captured images"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    part1=attach_file("image_set_1_0000.jpg")
    msg.attach(part1)
    part2=attach_file("image_set_1_0001.jpg")
    msg.attach(part2)
    part3=attach_file("image_set_1_0002.jpg")
    msg.attach(part3)
    part4=attach_file("gif_set_1.gif")
    msg.attach(part4)
  
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = '@gmail.com', password = '')  # User id & password
       #s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
       #print ("Error: unable to send email")    
    except smtplib.SMTPException as error:  
          print ("Error")                # Exception


def send_an_email5(toaddr):# image path setdef send_an_email():  
    #toaddr = '@gmail.com'      # To id 
    me = '@gmail.com'          # your id
    subject = "Captured images"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    part1=attach_file("image_set_2_0000.jpg")
    msg.attach(part1)
    part2=attach_file("image_set_2_0001.jpg")
    msg.attach(part2)
    part3=attach_file("image_set_2_0002.jpg")
    msg.attach(part3)
    part4=attach_file("image_set_2_0003.jpg")
    msg.attach(part4)
    part5=attach_file("image_set_2_0004.jpg")
    msg.attach(part5)
    part6=attach_file("gif_set_2.gif")
    msg.attach(part6)
  
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = '@gmail.com', password = '')  # User id & password
       #s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
       #print ("Error: unable to send email")    
    except smtplib.SMTPException as error:  
          print ("Error")                # Exception

def send_an_email10(toaddr):# image path setdef send_an_email():       # To id 
    me = '@gmail.com'          # your id
    subject = "Captured images"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    part1=attach_file("image_set_2_0000.jpg")
    msg.attach(part1)
    part2=attach_file("image_set_2_0001.jpg")
    msg.attach(part2)
    part3=attach_file("image_set_2_0002.jpg")
    msg.attach(part3)
    part4=attach_file("image_set_2_0003.jpg")
    msg.attach(part4)
    part5=attach_file("image_set_2_0004.jpg")
    msg.attach(part5)
    part6=attach_file("image_set_2_0005.jpg")
    msg.attach(part6)
    part7=attach_file("image_set_2_0006.jpg")
    msg.attach(part7)
    part8=attach_file("image_set_2_0007.jpg")
    msg.attach(part8)
    part9=attach_file("image_set_2_0008.jpg")
    msg.attach(part9)
    part10=attach_file("image_set_2_0009.jpg")
    msg.attach(part10)
    part11=attach_file("gif_set_3.gif")
    msg.attach(part11)
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = '@gmail.com', password = '')  # User id & password 
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()      
    except SMTPException as error:  
          print ("Error")                # Exception
