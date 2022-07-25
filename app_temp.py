from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import imghdr
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

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

# Shirts
@app.route('/uploadshirts')
def index_shirts():
    files = os.listdir('shirts')
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
        uploaded_file.save(os.path.join('shirts', filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload_shirts(filename):
    return send_from_directory('shirts', filename)


# Pants
@app.route('/uploadpants')
def index_pants():
    files = os.listdir('pants')
    return render_template('Upload_pants.html', files=files)

@app.route('/uploadpants', methods = ['POST'])
def Upload_pants():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join('pants', filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload_pants(filename):
    return send_from_directory('pants', filename)


# Shoes
@app.route('/uploadshoes')
def index_shoes():
    files = os.listdir('shoes')
    return render_template('Upload_shoes.html', files=files)

@app.route('/uploadshoes', methods = ['POST'])
def Upload_shoes():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join('shoes', filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload_shoes(filename):
    return send_from_directory('shoes', filename)

@app.route('/end')
def end():
    return "Return the value you want to see"


if __name__ == "__main__":
    app.run(debug=True)