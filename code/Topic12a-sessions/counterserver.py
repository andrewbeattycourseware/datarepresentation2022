from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'someSecrtetasdrgsdrge3ko'



@app.route("/")
def index():
    count=0
    count+=1

    if not 'counter' in session:
        session['counter'] =0
        print("new session")

    sessionCount=session['counter']
    sessionCount+=1
    session['counter']=sessionCount

    

    pageContent="<h1>counts</h1>" +\
        "session Count ="+str(sessionCount) +\
        "<br/>this Count ="+str(count)
    
    return pageContent

@app.route('/clear')
def clear():
    #session.clear()
    session.pop('counter',None)   

    return "done" 

if __name__ == '__main__' :
    app.run(debug= True)
