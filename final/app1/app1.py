# STEP 1 - IMPORT
from flask import Flask
from sqlalchemy import true

#STEP 2 - CREATE THE OBJECT

app = Flask(__name__)
users = ['anshika','kanav']
#STEP 3 - DEFINE A FUNC AND BIND IT WITH ROUTE
@app.route('/')
def index():
    return "WELCOME TO MY FIRST SERVER"

@app.route('/about')
def about_us():
    return "this is about us page!"

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in users:
        return "Welcome {}!".format(user_name)
    return "please register"

#RUN THE APP

if __name__ == '__main__':
    app.run(debug=true)