from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello World !</h1>"

@app.route('/newpage')
def info():
    return "<h2>Hello the Next page url</h2>"

@app.route('/puppy_latin/<name>')
def page(name):
    if name[::-1][0] == 'y':
        name = name.replace(name[len(name)-1], 'iful')
    else :
        name = name.replace(name[len(name)-1], 'y')
    return f"<h3>The Piglatin name is {name}</h3>"

if __name__ == '__main__':
    app.run()