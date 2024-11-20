from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/about')
def about():
    # Opret et svar med templaten
    response = make_response(render_template('about.html'))
    # Sæt cookien
    response.set_cookie('user_preference', 'dark_mode', max_age=3600)  # 1 time
    return response

@app.route('/get_cookie')
def get_cookie():
    # Læs cookien
    cookie_value = request.cookies.get('user_preference')
    return f"Cookie-værdi: {cookie_value}" if cookie_value else "Ingen cookie fundet!"

if __name__ == '__main__':
    app.run(debug=True)