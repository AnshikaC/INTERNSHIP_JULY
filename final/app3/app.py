from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def fun_1():
    if request.method == 'POST':
        Email = request.form['in_1']
        return "Welcome {}".format(Email)
    return render_template("Index.html")



#RUN THE APP

if __name__ == '__main__':
    app.run(debug=True)