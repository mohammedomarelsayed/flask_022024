from flask import Flask, abort, redirect, render_template, request, session, url_for
from flask import flash, Blueprint, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy 
# from flask_login import UserMixin
from datetime import datetime, timedelta

app = Flask(__name__)
# app.secret_key = "hello"
# connecting the db to project
# db = SQLAlchemy(app)
# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///database.db'
app.config['SECRET_KEY'] = 'A1B2C3D4E5F66F5E4D3C2B1A'
# app.permanent_session_lifetime = timedelta(miutes = 5)

# db = SQLAlchemy(app)
# def index():
#     return render_template('index.html',
#                            current_time=datetime.utcnow())
@app.route ('/')
def index():
        return render_template ('index.html')
# main = Blueprint('main', __name__)
# from . import views, errors

# @app.route('/tst')
# def tst():
#     return render_template('tst.html')


# @app.route('/tst2')
# def tst2():
#     return render_template('tst2.html')

# user's gretting algo.
    # @app.route('/user/<name>')
    # def user(name):
    #     return '<h1>Hello, %s!</h1>' % name


@app.route('/welcome')
def welcome():
    return render_template('welcome.html',
                           var_welcome_title= 'O_wellcome ',
                           page_head = 'X',
                           page_description = 'Y')
    
@app.route('/login')
def login():
    return render_template('login.html',
                           var_welcome_title= 'O_login ',
                           page_head = 'you login here_head',
                           page_description = 'description for loign page')

@app.route('/register')
def register():
    return render_template('register.html',
                           var_welcome_title= 'O_reg ',
                           page_head = 'reg head',
                           page_description = 'reg desc')

@app.route('/about')
def about():
    return render_template('about.html',
                           var_about_title = 'O_About ',
                           page_head = 'X',
                           description = 'Y')
    
@app.route('/tst2')
def tst():
    return render_template('tst2.html',
                           var_about_title = 'tst2 ',
                           page_head = 'X',
                           description = 'Y')    
    
    

    # flash ("about page flashing a msg")


# @app.route('/user/<name>' methods=['GET', 'POST'])
# def user(name):
#     return render_template('user.html', name=name)












if __name__ == '__main__':
    app.run (host ='0.0.0.0' ,debug=1)







# from flask.ext.bootstrap import Bootstrap
# # ...
# bootstrap = Bootstrap(app)

# error user's algo
# @app.route('/user/<id>')
# def get_user(id):
#      user = load_user(id)
#     if not user:
#         abort(404)  
#     return '<h1>Hello, %s</h1>' % user.name

# Example 2-3. hello.py: Using Flask-Script
# pip install flask-script
# from flask.ext.script import Manager
# manager = Manager(app)
# # ...
# if __name__ == '__main__':
#     manager.run()
# Extensions developed