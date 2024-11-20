from flask import Flask, request, redirect, render_template, make_response
import json
import os
from datetime import datetime

app = Flask(__name__, static_url_path="/", static_folder="static")

# File to store messages
MESSAGES_FILE = "messages.json"

# Load messages from disk or initialize
if os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "r") as file:
        messages = json.load(file)
else:
    messages = {}

# Home page
@app.route("/")
def home():
    return render_template("home.html", messages=messages)

# Write page
@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        
        # Validate inputs
        if not name or not message:
            return "Name and message cannot be empty!", 400
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save message
        messages[timestamp] = {"name": name, "message": message}
        
        # Save to disk
        with open(MESSAGES_FILE, "w") as file:
            json.dump(messages, file, indent=4)
        
        # Store name in cookie
        resp = make_response(redirect("/"))
        resp.set_cookie("name", name)
        return resp
    
    # Pre-fill name from cookie if available
    name = request.cookies.get("name", "")
    return render_template("write.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, port=8080)