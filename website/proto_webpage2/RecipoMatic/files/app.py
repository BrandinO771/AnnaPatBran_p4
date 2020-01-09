
import os
import re

import webbrowser
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, redirect,  url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory

import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

# THIS IS THE LOCATION OF OUR IMAGES 
UPLOAD_FOLDER = 'images'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    # return "Welcome to my 'Home' page!"
    return render_template("index.html")


# CALL IMAGE BY FILE NAME TO RENDER IN WEBPAGE 
# 'WORKS BELOW JUST TYPE IN /show/robot1.jpg'  
# '---and the image will appear' 
@app.route('/show/<filename>')
def uploaded_file(filename):
    print('Hello I am the --UPLOADED_FILE FUNCTION-- : this is the file name' , filename)
    print('from uploaded file the file name is', filename)
    return render_template('index.html', filename=filename)

# DIRECTLY OPEN IMAGE PAGE BY ITSELF - MAY WORK IN TANDOM WITH  UPLOADED FILE FUNC ABOVE
@app.route('/uploads/<filename>')
def send_file(filename):
 
    print('---------------------------------------')
    print('THE send_file Funciton is being called>>>>>>>>!!' )
    print('from send file the file name is', filename)
    print('---------------------------------------')
    uploaded_file(filename)
    return send_from_directory(UPLOAD_FOLDER, filename)



@app.route('/load_image/', methods=['GET', 'POST']   )
def test_submit():
    print(">>>>>>--The request.method is:", request.method )
    if request.method =="GET":
        print(">>>>>>--The request form get:", request.form.get)
        print(">>>>>>--The request form get file:", request.form.get('name'))
        print(">>>>>>--The request form get GET:", request.form.get('GET'))
    if request.method =="POST":
        print(">>>>>>--The request form get:", request.form.get)
        ### below this gives us the name of the image file 
        print(">>>>>>--The request form get file:", request.form.get('file'))
        image_name =  request.form.get('file')
        print(">>>>>>--The request form get GET:", request.form.get('POST'))
        #CALL FUNCTION ABOVE
        uploaded_file(request.form.get('file'))
        # @app.route = ('/show/'+image_name)

    print(">>>>>>--The request form  :", request.form )
    print(">>>>>>--The request   :", request )
    return redirect('/show/'+image_name)
    # return render_template('index.html')  





# def send_file(filename): 
#     return send_from_directory(UPLOAD_FOLDER, filename ),redirect("/")



@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
    # return    <img  src="img_chania.jpg" alt="Flowers in Chania">



if __name__ == "__main__":
    app.run(debug=True)


# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////




# //////////////////////////////////////////////////////////////////////
# ///////BELOW WORKS TO DISPLAY AN IMAGE FROM OUR IMAGE FOLDER/////
# //////////////////////////////////////////////////////////////////////
# @app.route('/uploads/')
# def uploaded_file():
#     print('THE uploaded_file is being called>>>>>>>>!!' )
#     print('---------------------------------------')
#     image = (send_from_directory(app.config['UPLOAD_FOLDER'],'robot1.jpg'))
#     print('the image is' ,  image)
#     return image



# @app.route('/show/?file=robot1.jpg')
# def test_file(filename):
#     print('this is the file name' , filename)
#     # name = filename.split("=")
#     # print("this is the name split", name)
#     # filename = 'http://127.0.0.1:5000/uploads/' + filename
#     # filename =  name
#     # print('from uploaded file the file name is', filename)
#     # return render_template('index.html', filename=filename)
#     return






#/////   FORCE OPEN ANY WEBSITE //////////////
# @app.route('/show/?myFile=<name>')
# webbrowser.open_new(url)
# url = 'http://127.0.0.1:5000/'
# webbrowser.open(url, new=0, autoraise=True)
# url = 'http://127.0.0.1:5000/show/chef1.jpg' 
# webbrowser.open(url, new=0, autoraise=True)
#/////   FORCE OPEN ANY WEBSITE //////////////



# @app.route('/show/<filename>')
# def uploaded_file(filename):
#     filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('template.html', filename=filename)

# @app.route('/uploads/<filename>')
# def send_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# <!doctype html>
# <title>Hello from Flask</title>
# {% if filename %}
#   <h1>some text <img src="{{ url_for('send_file', filename=filename) }}">more text!</h1>
# {% else %}
#   <h1>no image for whatever reason</h1>
# {% endif %}

# @app.route('/img/<filename>') 




# def show(id):
#     photo = Photo.load(id)
#     if photo is None:
#         abort(404)
#     url = photos.url(photo.filename)
#     return render_template('show.html', url=url, photo=photo)


# Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url + 'doc/')
# @app.route('/show/<filename>')
# def uploaded_file(filename):
#     print('this is the file name' , filename)


    # return render_template('index.html', filename=filename)