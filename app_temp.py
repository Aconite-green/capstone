from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import imghdr
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

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
                    return redirect(url_for('index_shirts'))
                else:
                    return 'Wrong Password!'
            return 'ID does not exist'
        except:
            return 'Sorry get out'
    else:
        return render_template('Login.html')

# get image data
@app.route('/uploadshirts')
def index_shirts():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('Upload_shirts.html', files=files)

@app.route('/uploadshirts', methods = ['POST'])
def Upload_shirts():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(debug=True)