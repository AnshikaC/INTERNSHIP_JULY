from flask import Flask, render_template, request
import re

regex101 = Flask(__name__)


@regex101.route('/', methods=["POST","GET"])
def index():
    m = []
    if request.method=="POST":
        exp = request.form['expression']
        match = request.form['find_string']

        pattern = re.compile(exp)
        n = match

        total = len(pattern.findall(n))
        matched = pattern.findall(n)

        
        matching = pattern.search(match)
        m.append(matching)
        
        
        return render_template('index.html', m=m, a = total)
    return render_template('index.html')

    
    
    
    
if __name__=="__main__":
    
    regex101.run(debug=True)