from flask import Flask
from flask import request
import requests
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/test',methods=['POST','GET'])
def test():
    URL = "http://172.16.6.203:3030/analyse"
    data = ''
    if request.method == 'POST':
        print("Hiiiiii")
        git_url = request.form.get("git_url")
        print(git_url)
        PARAMS = {"git_repo":git_url}
        r = requests.get(url = URL, json = PARAMS)
        data = r.json()
        print(data)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)