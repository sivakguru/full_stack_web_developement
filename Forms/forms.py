from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/thanks')
def thanks():
    first = request.args.get('first')
    last = request.args.get('last')
    checkbox = request.args.get('checkbox')
    if checkbox == 'remember':
        val='We will Remember you..!'
    else:
        val='We wont Save any cache..!'
    return render_template('thanks.html', first=first, last=last, checkbox=val)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()