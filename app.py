from flask import Flask, render_template, request, redirect
import os
from models import db, User
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

# sign in!
@app.route('/register', methods = ['GET','POST'])
def Register():
    if request.method =='GET':
        return render_template('Register.html')
    else:
        userid =request.form.get('userid')
        email = request.form.get('email')
        password = request.form.get('password')

        if not(userid and email and password):
            return "Please fill in all blanks"
        else:
            usertable = User()
            usertable.userid = userid
            usertable.email = email
            usertable.password = password

            db.session.add(usertable)
            db.session.commit()
            return "Membership successful"
        return redirect('/login')
        


# get image data
@app.route('/upload', methods = ['POST'])
def Upload():
    pass

# show image using model
@app.route('/items', methods = ['POST'])
def Items():
    pass



# show image using model
@app.route('/login', methods = ['POST'])
def Login():
    pass

# show image using model
@app.route('/closet', methods = ['POST'])
def Closet():
    pass



if __name__ == "__main__":
    #데이터베이스---------
    basedir = os.path.abspath(os.path.dirname(__file__)) #현재 파일이 있는 디렉토리 절대 경로
    dbfile = os.path.join(basedir, 'db.sqlite') #데이터베이스 파일을 만든다

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다

#    db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장
    db.init_app(app) #app설정값 초기화
    db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
    db.create_all() #DB생성

    app.run(host="127.0.0.1", port=5000, debug=True)