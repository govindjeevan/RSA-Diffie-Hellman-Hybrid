from flask import Flask
from flask import request
import Hybrid
from flask import render_template
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("my_form.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    data= Hybrid.hybrid(text)
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run()
