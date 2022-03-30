from Cloner import Cloner
import uuid
from flask import Flask, request,jsonify



app = Flask(__name__)



@app.route('/clone')
def analyse():
    data = request.get_json()
    print(data)
    git_url = data['git_repo']
    uuid = data['uuid']
    destination = './'
    cloner = Cloner(git_url,str(uuid.uuid1()),destination)
    cloner.clone()

    return git_url

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3030,debug = False)	