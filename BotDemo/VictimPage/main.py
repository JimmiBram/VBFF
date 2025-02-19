from flask import Flask, request, render_template_string
from flask_socketio import SocketIO
import time

# Set the maximum pagehits value (for the last 60 seconds)
MAX_PAGEHITS = 100

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# List to store hit data.
# Each hit is a dict: { 'timestamp': float, 'ip': str, 'response_time': float }
hits = []

def get_recent_hits():
    """Return hits from the last 60 seconds."""
    cutoff = time.time() - 60
    return [hit for hit in hits if hit['timestamp'] >= cutoff]

def broadcast_update():
    """Broadcast the current hit count and log to all clients."""
    recent_hits = get_recent_hits()
    data = {
        'count': len(recent_hits),
        'hits': recent_hits
    }
    # Removed the broadcast=True option (it is now broadcast by default)
    socketio.emit('update', data)

@app.route('/')
def index():
    start_time = time.time()
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Very important page</title>
      <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 0; }
        #header { display: flex; justify-content: space-between; align-items: center; background: #eee; padding: 20px; }
        #title { font-size: 36px; font-weight: bold; }
        #clock { font-size: 24px; }
        #content { padding: 20px; }
        #gauge-container { width: 300px; margin: 20px auto; }
        #log { max-width: 600px; margin: 20px auto; text-align: left; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        /* Traffic warning overlay */
        #traffic-warning {
          display: none;
          position: fixed;
          top: 5%;
          left: 5%;
          width: 90%;
          height: 90%;
          background-color: rgba(255, 0, 0, 0.5);
          z-index: 1000;
          align-items: center;
          justify-content: center;
          font-size: 36px;
          color: white;
        }
      </style>
      <!-- Socket.IO client library -->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.6.1/socket.io.min.js"></script>
      <!-- Gauge.js library -->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/gauge.js/1.3.7/gauge.min.js"></script>
      <script>
        // Pass the MAX_PAGEHITS constant from Flask into JavaScript.
        const MAX_PAGEHITS = {{ max_pagehits }};
      </script>
    </head>
    <body>
      <!-- Warning overlay (hidden by default) -->
      <div id="traffic-warning">Page is down due to too much traffic</div>
      <div id="header">
        <div id="title">Very important page</div>
        <div id="clock"></div>
      </div>
      <div id="content">
        <!-- The header text will be updated to "X pagehits last 60 seconds" -->
        <div id="pagehits-text">0 pagehits last 60 seconds</div>
        <div id="gauge-container">
          <canvas id="gauge-canvas" width="300" height="150"></canvas>
        </div>
        <div id="log">
          <h3>Hit Log (last 60 seconds)</h3>
          <table id="log-table">
            <thead>
              <tr>
                <th>IP Address</th>
                <th>Response Time (ms)</th>
                <th>Timestamp</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
      <script>
        // Update clock every second.
        function updateClock() {
          var now = new Date();
          document.getElementById('clock').innerText = now.toLocaleTimeString();
        }
        setInterval(updateClock, 1000);
        updateClock();

        // Set up the gauge (speedometer).
        var opts = {
          angle: 0, // The span of the gauge arc.
          lineWidth: 0.2, // The line thickness.
          radiusScale: 1, // Relative radius.
          pointer: {
            length: 0.6,  // Relative to gauge radius.
            strokeWidth: 0.035,
            color: '#000000'
          },
          limitMax: false,
          limitMin: false,
          // Initial color is set to green.
          colorStart: '#00ff00',
          colorStop: '#00ff00',
          strokeColor: '#E0E0E0',
          generateGradient: true,
          highDpiSupport: true
        };
        var target = document.getElementById('gauge-canvas');
        var gauge = new Gauge(target).setOptions(opts);
        gauge.maxValue = MAX_PAGEHITS; // Use constant for max value.
        gauge.setMinValue(0);
        gauge.animationSpeed = 32;
        gauge.set(0);

        // Connect to the Socket.IO server.
        var socket = io();

        socket.on('connect', function() {
          console.log('Connected to server');
        });

        // Listen for updates from the server.
        socket.on('update', function(data) {
          console.log('Received update:', data);
          // Calculate percentage relative to MAX_PAGEHITS.
          var percentage = data.count / MAX_PAGEHITS;
          var newColor = "";
          if (percentage >= 0.8) {
            newColor = "#ff0000"; // red when above 80%
          } else if (percentage >= 0.3) {
            newColor = "#ffa500"; // orange when between 30% and 80%
          } else {
            newColor = "#00ff00"; // green when below 30%
          }
          // Update the gauge colors.
          gauge.options.colorStart = newColor;
          gauge.options.colorStop = newColor;
          gauge.set(Math.min(data.count, MAX_PAGEHITS));

          // Update the pagehits text with the current count.
          document.getElementById('pagehits-text').innerText = data.count + " pagehits last 60 seconds";

          // Update the log table.
          var tbody = document.querySelector('#log-table tbody');
          tbody.innerHTML = '';
          // Sort hits by most recent first.
          data.hits.sort(function(a, b) { return b.timestamp - a.timestamp; });
          data.hits.forEach(function(hit) {
            var tr = document.createElement('tr');
            var tdIp = document.createElement('td');
            tdIp.innerText = hit.ip;
            var tdResp = document.createElement('td');
            // Convert response time from seconds to milliseconds.
            tdResp.innerText = (hit.response_time * 1000).toFixed(2);
            var tdTime = document.createElement('td');
            var d = new Date(hit.timestamp * 1000);
            tdTime.innerText = d.toLocaleTimeString();
            tr.appendChild(tdIp);
            tr.appendChild(tdResp);
            tr.appendChild(tdTime);
            tbody.appendChild(tr);
          });

          // If the maximum pagehits is reached, show the warning overlay.
          var warningBox = document.getElementById('traffic-warning');
          if (data.count >= MAX_PAGEHITS) {
            warningBox.style.display = "flex";
          } else {
            warningBox.style.display = "none";
          }
        });
      </script>
    </body>
    </html>
    """
    response = render_template_string(html, max_pagehits=MAX_PAGEHITS)
    elapsed = time.time() - start_time

    # Record this hit.
    hit = {
        'timestamp': time.time(),
        'ip': request.remote_addr,
        'response_time': elapsed
    }
    hits.append(hit)

    # Remove any hits older than 60 seconds.
    cutoff = time.time() - 60
    hits[:] = [h for h in hits if h['timestamp'] >= cutoff]

    broadcast_update()
    return response

@socketio.on('connect')
def handle_connect():
    recent_hits = get_recent_hits()
    socketio.emit('update', {'count': len(recent_hits), 'hits': recent_hits}, to=request.sid)

def background_updater():
    """Background task: every second, purge expired hits and update clients."""
    while True:
        socketio.sleep(1)
        cutoff = time.time() - 60
        hits[:] = [h for h in hits if h['timestamp'] >= cutoff]
        broadcast_update()

if __name__ == '__main__':
    socketio.start_background_task(background_updater)
    socketio.run(app, port=8080)