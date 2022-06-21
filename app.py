from flask import Flask, render_template, request, redirect, url_for
import os


# For getting image data
# import pickle
# import numpy as np 

# load model.py
# model = pickle.load(open('filename.pkl', 'rb'))

app = Flask(__name__)

# show Home page
@app.route('/')
def Landing():
    return render_template('Landing.html')


userinfo = {'po' : 'po'}
# sign in!
@app.route('/register', methods = ['GET','POST'])
def Register():
    if request.method == 'POST':
        userinfo[request.form['username']] = request.form['password']
        return redirect(url_for('Login'))
    else:
        return render_template('Register.html')
    


# show image using model
@app.route('/login', methods = ['Get', 'POST'])
def Login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        try:
            if name in userinfo:
                if userinfo[name] == password:                  
                    return redirect(url_for('Upload'))
                else:
                    return 'Wrong Password!'
            return 'ID does not exist'
        except:
            return 'Sorry get out'
    else:
        return render_template('Login.html')

# get image data
@app.route('/upload', methods = ['GET', 'POST'])
def Upload():
    return render_template('Upload.html')

# show image using model
@app.route('/items', methods = ['POST'])
def Items():
    pass

# show image using model
@app.route('/closet', methods = ['POST'])
def Closet():
    pass



if __name__ == "__main__":
   
    app.run(host="127.0.0.1", port=5000, debug=True)