#main flask app that serves the html pages and gets the python backend script to run

from flask import Flask, render_template, request
from facerecog_main import *
import warnings
from flask_ngrok import run_with_ngrok
warnings.simplefilter("ignore", DeprecationWarning)

app=Flask(__name__)
#run_with_ngrok(app)
@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        useremail=request.form["email"]       # getting the email id from the form
        userno=request.form["snaps"]          # getting the number of snaps
        if(userno=='10'):                     # for 10 snaps
            run_camera_recog(3,1)
            send_an_email10(useremail)
        elif(userno=='5'):                    # for 5 snaps
            run_camera_recog(2,1)
            send_an_email5(useremail)
        else:
            run_camera_recog(1,1)             #for 3 snaps
            send_an_email3(useremail)
        return render_template('second2.html')        # returning the page of confirmation
    return render_template('index.html')              # returning the main page

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
    
