from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/', methods=['GET'])
def getAllBands():
    return "hello from simple server"


if __name__ == "__main__":
    app.run(debug=True)