from flask import Flask,render_template,flash,redirect,request
from dbhelper import *


app = Flask(__name__)

uploadfolder="static/img"
#@app.config['SECRET_KEY']='!@#$%^'
app.secret_key = '!@#$%^'
app.config['UPLOAD_FOLDER'] = uploadfolder

@app.route("/savestudent",methods=['POST','GET'])
def savestudent()->None:
    idno:str = request.args.get('idno')
    lastname:str = request.args.get('lastname')
    firstname:str = request.args.get('firstname')
    course:str = request.args.get('course')
    level:str = request.args.get('level')
    imagename:str = uploadfolder +"/"+idno+".jpg"

    file = request.files['webcam']
    file.save(imagename)
    
    ok:bool = add_record('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=imagename)
    message = "New Student Added" if ok else "Error Adding Student"
    flash(message)
    return redirect("/")
    
@app.route("/")
def index()->None:
    return render_template("index.html",pagetitle="Student Information")
    

if __name__=="__main__":
    app.run(debug=True)