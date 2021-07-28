from flask import Flask, app, render_template, request
import re

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
    uname = request.args.get('uname')
    checkbox = request.args.get('checkbox')
    val = 'We will Remember you..!' if checkbox == 'remember' else 'We wont Save any cache..!'
    # User name Validation
    validation = {
        '[0-9]$':'Must Have a Number at the END',
        '[A-Z]':'Must have an Uppercase',
        '[a-z]':'Must have a lowercase'
    }
    test_val = [validation[x] if not bool(re.search(x,uname)) else 'pass' for x in list(validation.keys())]
    not_valid = [x for x in test_val if x!='pass']
    check=len(not_valid)
    return render_template('thanks.html', first=first, last=last,
     checkbox=val, not_valid=not_valid, check=check)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)