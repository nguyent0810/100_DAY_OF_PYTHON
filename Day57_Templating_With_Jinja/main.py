from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    my_name = "Tung Nguyen"
    return render_template("index.html", num=random_number, current_year=current_year, my_name=my_name)
@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    data = gender_response.json()
    gender = data['gender']
    age_response = requests.get(url=f'https://api.agify.io?name={name}')
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    blog_url = 'https://api.npoint.io/5da281d06062f7a0f414'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)