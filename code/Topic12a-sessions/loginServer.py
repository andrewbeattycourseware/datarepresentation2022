from flask import Flask, session, url_for,redirect, abort
app = Flask(__name__)
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'


@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    
    return 'welcome ' + session['username'] +\
        '<br><a href="'+url_for('logout')+'">logout</a>'

@app.route('/login')
def login():
    return '<h1> login</h1> '+\
        '<button>'+\
            '<a href="'+url_for('proccess_login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'

@app.route('/processlogin')
def proccess_login():
    #check credentials
    #if bad redirect to login page again

    #else
    session['username']="I dunno"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


@app.route('/data')
def getData():
    if not 'username' in session:
        abort(401)
    # user is authoristed
    return '{"data":"all here"}'

if __name__ == '__main__' :
    app.run(debug= True)

