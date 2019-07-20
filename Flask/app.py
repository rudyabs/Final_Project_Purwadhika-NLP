from flask import Flask, render_template, url_for

app = Flask(__name__)

# dummy post data
posts = [
    {
        'author':'Rudy',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'July 20, 2019'
    },
    {
        'author':'Aunallah',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'July 21, 2019'
    }
]



@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
