from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get user information
    full_name = "Your Full Name"  # Replace with your full name
    username = os.getlogin()

    # Get server time in IST
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get the 'htop' output using subprocess
    htop_output = subprocess.getoutput('top -b -n 1')

    # Create the HTML output
    return f"""
    <h3>Name: {full_name}</h3>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>Top output:\n{htop_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
