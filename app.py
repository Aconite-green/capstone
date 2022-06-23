from flask import Flask, render_template, request, redirect, url_for
import os
import sys

from werkzeug.utils import secure_filename

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
                    return redirect(url_for('Upload_hat'))
                else:
                    return 'Wrong Password!'
            return 'ID does not exist'
        except:
            return 'Sorry get out'
    else:
        return render_template('Login.html')

# get image data
@app.route('/uploadhat', methods = ['GET', 'POST'])
def Upload_hat():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return "uploaded successfully"
    else:
        return render_template('Upload_hat.html')
    

@app.route('/uploadouter', methods = ['GET', 'POST'])
def Upload_outer():
        return render_template('Upload_outer.html')



if __name__ == "__main__":
   
    app.run(debug=True)