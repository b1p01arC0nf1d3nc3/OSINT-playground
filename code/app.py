# an object of WSGI application 
import os
import json
from urllib.parse import urlparse
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__) # Flask constructor 


#-----------------------------------------------------------------------
# instasham
#-----------------------------------------------------------------------
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/instasham')
def instasham():
    return 'instasham will go here.'


#the below dynamically adds the user to url and adds it in output
@app.route('/instasham/user/<name>')
def instashamUsers(name):
    return 'Hello %s. Welcome to Instasham.' % name


#-----------------------------------------------------------------------
# FauxTube
#-----------------------------------------------------------------------
@app.route('/fauxtube')  #decorator for route(argument) function 
def fauxtube():     #binding to fauxtube call
   #returning the specific html index page.
   return render_template('/fauxtube/fauxtubeindex.html')    
  

@app.route('/guest/<guest>') 
def hello_guest(guest):    #binding to hello_guest call 
   return 'Hello %s as Guest' % guest 

#the function below will take in a username and redirect it  
@app.route('/user/<name>') 
def hello_user(name):     
   if name =='admin':  #dynamic binding of URL to function 
      return redirect(url_for('hello_admin'))   
   else: 
      return redirect(url_for('hello_guest', guest = name))
   

#-----------------------------------------------------------------------
# homepage/challenges
#-----------------------------------------------------------------------   
#this function defines which template file will be returned using render_template
#the root starts in /template/, which will be similar for /static/   
@app.route("/")
def homepage():
   return render_template('homepageindex.html')

if __name__=='__main__': 
    app.run()
