import uuid
from flask import Flask, request,jsonify
import requests
import json 
CLONER_MODULE_URL = "http://35.188.213.6:3030/clone"
app = Flask(__name__)



@app.route('/analyze')
def analyze():
    data = request.get_json()
    git_url = data['git_repo']
    print(data)
    PARAMS = {'git_repo':git_url,'uuid':'aaaaaa'}
    jsonData = json.dumps(PARAMS)
    r = requests.get(url = CLONER_MODULE_URL,json=jsonData)
    # extracting data in json format
    #data = r.json()


    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3030,debug = False)	