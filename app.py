from flask import Flask, render_template, request, redirect, url_for
import os
import sys

from werkzeug.utils import secure_filename
# how to do it
app = Flask(__name__)

# show Home page
@app.route('/')
def Landing():
    return render_template('Landing.html')


userinfo = {'po' : 'po'}
# sign in!
@app.route('/signup', methods = ['GET','POST'])
def Register():
    if request.method == 'POST':
        userinfo[request.form['username']] = request.form['password']
        return redirect(url_for('Login'))
    else:
        return render_template('Signup.html')
    


# show image using model
@app.route('/login', methods = ['Get', 'POST'])
def Login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        try:
            if name in userinfo:
                if userinfo[name] == password:                  
                    return redirect(url_for('Upload_shirts'))
                else:
                    return 'Wrong Password!'
            return 'ID does not exist'
        except:
            return 'Sorry get out'
    else:
        return render_template('Login.html')

# get image data
@app.route('/uploadshirts', methods = ['GET', 'POST'])
def Upload_shirts():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return "uploaded successfully"
    else:
        return render_template('Upload_shirts.html')
    


if __name__ == "__main__":
    app.run(debug=True)