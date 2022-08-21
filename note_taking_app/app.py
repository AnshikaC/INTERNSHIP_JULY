from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/' , methods=['post','get'])
def index():
    if request.method!='post':
        note = request.args.get('note')
        if note != None:
            notes.append(note)
            return render_template("home.html", notes=notes)
        return render_template("home.html")
    return "Nothing"


if __name__ == '__main__':
    app.run(debug=True)