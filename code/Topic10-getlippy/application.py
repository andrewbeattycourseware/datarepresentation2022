from flask import Flask, jsonify, abort, request
from votedao import voteDAO

app = Flask(__name__, static_url_path='', static_folder='static')

bands = [
    {'name':'band1'},
    {'name':'band2'},
    {'name':'climbing club'},
    ]

@app.route('/band', methods=['GET'])
def getAllBands():
    return jsonify(bands)

@app.route('/vote/<bandname>', methods=['POST'])
def voteForBand(bandname):
    ip_addr = request.remote_addr
    data = (bandname, ip_addr)
    newid = voteDAO.create(data)

    return jsonify({'id':newid})

@app.route('/vote/<bandname>', methods=['GET'])
def getCountForBand(bandname):
    count = voteDAO.countvotes(bandname)
    return jsonify({bandname:count})

@app.route('/vote', methods=['GET'])
def getAllCount():
    allcounts = []
    for band in bands:
        bandname = band['name'] 
        count = voteDAO.countvotes(bandname)
        allcounts.append({bandname:count})
    return jsonify(allcounts)

@app.route('/vote/all', methods=['delete'])
def deleteAllVote():
    return jsonify({'done':True})



if __name__ == "__main__":
    app.run(debug=True)