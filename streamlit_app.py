import streamlit as st
import subprocess
import time
import requests
import pandas as pd
from pyngrok import ngrok

# Function to start Flask in background with unbuffered output
def start_flask():
    return subprocess.Popen(
        ["python", "app.py"], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        text=True,
        bufsize=1  # Unbuffered output for real-time logs
    )

# Function to fetch logs in real-time
def get_logs(process):
    logs = []
    while True:
        line = process.stdout.readline()  # Read line-by-line instead of looping over process.stdout
        if not line:
            continue  # Keep waiting for new logs
        line = line.strip()
        logs.append(line)
        if len(logs) > 10:  # Limit logs to last 10 entries
            logs.pop(0)
        yield logs

# Streamlit UI
st.title("🔍 Flask Tracking App with Ngrok")

# Start Flask App
st.subheader("Starting Flask Server... ⏳")
flask_process = start_flask()
time.sleep(3)  # Give Flask time to start

# Start ngrok tunnel
st.subheader("Starting Ngrok Tunnel... 🚀")
ngrok_tunnel = ngrok.connect(5000)
tracking_url = f"{ngrok_tunnel.public_url}/track?user_id=123"

# Display the generated tracking link
st.success(f"Generated Tracking Link: [Click here]({tracking_url})")
st.code(tracking_url, language="markdown")

# Capture and display Flask logs
st.subheader("📜 Flask Logs")
log_container = st.empty()

# Continuously update logs
for logs in get_logs(flask_process):
    if logs:
        df_logs = pd.DataFrame({"Logs": logs})
        log_container.table(df_logs)

# Stop Flask on app exit
st.warning("To stop Flask and Ngrok, close this Streamlit app.")
