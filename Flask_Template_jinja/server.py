import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get('https://api.genderize.io/?name='+name)
    age = requests.get('https://api.agify.io/?name='+name)
    gender = gender.json()
    age = age.json()
    # print(gender.get('gender'), age.get('age'))
    return render_template('index.html',prop={'name': name,
                                              'age': age.get('age'), 'gender': gender.get('gender')})

if __name__ == '__main__':
    app.run(debug=True)