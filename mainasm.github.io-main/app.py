from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'

db = SQLAlchemy (app)

class Task(db.Model):
     id = db.Column(db.Integer, primary_key= True)
     fName = db.Column(db.String(400), nullable = False)
     lName = db.Column(db.String(400), nullable = False)
     eMail = db.Column(db.String(400), nullable = False)
     message = db.Column(db.String(400), nullable = False)
     date_added = db.Column (db.DateTime, default= datetime.utcnow)

     def __tsl__(self):
         return '<Task %r>' &self.id


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/contact', methods = ['POST','GET'])
def contact():
    
    if request.method == "POST":
    
      contact = Task(fName= request.form['firstname'], lName=request.form['lastName'], eMail= request.form['email'], message=request.form['message'] )

      try:
          db.session.add(contact)
          db.session.commit
          return redirect('/')
      except:
              return "There is an error adding contact information"
    else:
        return render_template("contact.html")
          
    

if __name__ == '__main__':
   app.run(debug = True)







