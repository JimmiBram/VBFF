pip install flask

Create structure:
flask_example/
├── app.py
├── templates/
│   ├── home.html
│   └── about.html


app.py
from flask import Flask, render_template

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html', title="Home")

# Define the about route
@app.route('/about')
def about():
    return render_template('about.html', title="About")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)





home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to the Home Page!</h1>
    <p>This is a simple Flask website example.</p>
    <a href="/about">Go to About Page</a>
</body>
</html>


about.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>About This Website</h1>
    <p>This website is a demonstration of a simple Flask app.</p>
    <a href="/">Go back to Home</a>
</body>
</html>


Run:
python app.py


Open in Browser
Open your browser and go to http://127.0.0.1:5000/. You should see the home page, and clicking the link will take you to the about page.

This example covers the basics of Flask routing and templating, providing a foundation for building a dynamic website.