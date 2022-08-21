# STEP 1 - IMPORT
from flask import Flask, render_template


#STEP 2 - CREATE THE OBJECT

app = Flask(__name__)


@app.route('/')
def fun_1():
    return render_template("Index.html")
#RUN THE APP

if __name__ == '__main__':
    app.run(debug=True)