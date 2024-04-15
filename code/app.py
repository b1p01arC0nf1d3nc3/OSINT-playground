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
@app.route('/instasham/')
def instasham():
    return render_template('/instasham/instashamindex.html')

#example post page
@app.route('/instasham/post1')
def instashamPost1():
   return render_template('/instasham/instapost.html')

@app.route('/instasham/user1')
def instashameUser1():
   return render_template('instasham/instauser1.html')


#the below dynamically adds the user to url and adds it in output
#@app.route('/instasham/user/<name>')
#def instashamUsers(name):
#    return 'Hello %s. Welcome to Instasham.' % name


#-----------------------------------------------------------------------
# FauxTube
#-----------------------------------------------------------------------
@app.route('/fauxtube')  #decorator for route(argument) function 
def fauxtube():     #binding to fauxtube call
   #returning the specific html index page.
   return render_template('/fauxtube/fauxtubeindex.html')

@app.route('/fauxtube/vid1')   
def fauxtubevid1():
   #returns the html for vid1
   return render_template('fauxtube/vid1.html')

@app.route('/fauxtube/vid2')   
def fauxtubevid2():
   #returns the html for vid1
   return render_template('fauxtube/vid2.html') 

@app.route('/fauxtube/vid4')   
def fauxtubevid4():
   #returns the html for vid1
   return render_template('fauxtube/vid4.html') 

@app.route('/fauxtube/vid5')   
def fauxtubevid5():
   #returns the html for vid1
   return render_template('fauxtube/vid5.html') 

@app.route('/fauxtube/vid6')   
def fauxtubevid6():
   #returns the html for vid1
   return render_template('fauxtube/vid6.html') 

@app.route('/fauxtube/vid7')   
def fauxtubevid7():
   #returns the html for vid1
   return render_template('fauxtube/vid7.html') 

@app.route('/fauxtube/vid8')   
def fauxtubevid8():
   #returns the html for vid1
   return render_template('fauxtube/vid8.html') 

@app.route('/fauxtube/vid9')   
def fauxtubevid9():
   #returns the html for vid1
   return render_template('fauxtube/vid9.html') 

@app.route('/fauxtube/vid10')   
def fauxtubevid10():
   #returns the html for vid1
   return render_template('fauxtube/vid10.html') 

@app.route('/fauxtube/vid11')   
def fauxtubevid11():
   #returns the html for vid1
   return render_template('fauxtube/vid11.html') 

@app.route('/fauxtube/vid12')   
def fauxtubevid12():
   #returns the html for vid1
   return render_template('fauxtube/vid12.html')  

@app.route('/fauxtube/<string:youtube_video_id>')
def video_page(youtube_video_id):
   return render_template('fauxtube/vid.html', youtube_video_id=youtube_video_id)
  


   
#-----------------------------------------------------------------------
# homepage/challenges
#-----------------------------------------------------------------------   
#this function defines which template file will be returned using render_template
#the root starts in /template/, which will be similar for /static/   
@app.route("/")
def homepage():
   return render_template('homepage/homepageindex.html')

@app.route("/challenges")
def challenges():
   return render_template('homepage/challenges.html')

#challenge room routes
@app.route("/challenges/1")
def challenge1():
   return render_template('homepage/challenges/1.html')
@app.route("/challenges/2")
def challenge2():
   return render_template('homepage/challenges/2.html')
@app.route("/challenges/3")
def challenge3():
   return render_template('homepage/challenges/3.html')
@app.route("/challenges/4")
def challenge4():
   return render_template('homepage/challenges/4.html')
@app.route("/challenges/5")
def challenge5():
   return render_template('homepage/challenges/5.html')
@app.route("/challenges/6")
def challenge6():
   return render_template('homepage/challenges/6.html')
@app.route("/challenges/7")
def challenge7():
   return render_template('homepage/challenges/7.html')
@app.route("/challenges/8")
def challenge8():
   return render_template('homepage/challenges/8.html')
@app.route("/challenges/9")
def challenge9():
   return render_template('homepage/challenges/9.html')
@app.route("/challenges/10")
def challenge10():
   return render_template('homepage/challenges/10.html')


@app.route("/sites")
def sites():
   return render_template('homepage/sites.html')

@app.route("/tools")
def tools():
   return render_template('homepage/tools.html')
   

if __name__=='__main__': 
    app.run(host="0.0.0.0")
