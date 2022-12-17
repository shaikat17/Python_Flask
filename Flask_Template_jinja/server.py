import requests
from flask import Flask, render_template, url_for

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

@app.route('/blog')
def blog():
    blog_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template('blog.html', posts=all_posts)

@app.route('/post/<index>')
def show_post(index):
    blog_url = 'https://jsonplaceholder.typicode.com/posts/'+index
    response = requests.get(blog_url)
    post = response.json()
    print(post)

    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)