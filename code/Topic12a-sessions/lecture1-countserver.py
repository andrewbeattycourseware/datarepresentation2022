from flask import Flask, session
app = Flask(__name__)

app.secret_key = 'someSecrtetasdrgsdrge3ko'


@app.route('/')
def index():
    count = 0
    if not 'counter' in session:
        session['counter'] = 0
    else:
        count = session['counter']
        count = count + 1
        session['counter'] = count
    return "hello world" + str(count)

@app.route('/clear')
def clear():
    session.pop('counter', None)
    return "counter cleared"

if __name__ == '__main__' :
    app.run(debug= True)
