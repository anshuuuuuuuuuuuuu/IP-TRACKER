# IP Tracker  

## Overview  
This is an IP tracking tool designed to identify and monitor suspicious users. It generates a tracking link using **Ngrok** and logs visitor details such as IP addresses, location, and user agent.  

## Features  
- **Ngrok Integration** – Creates a publicly accessible tracking link  
- **IP Logging** – Captures IP addresses of visitors  
- **Geolocation** – Retrieves approximate location data  
- **User-Agent Tracking** – Identifies device, OS, and browser  
- **Stealth Mode** – Minimal footprint for tracking users discreetly  

## Installation  

### Prerequisites  
- Python 3.x  
- Ngrok (installed and authenticated)  
- Required Python modules:  
  ```bash
  pip install flask requests
  ```  

### Setup  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/anshuuuuuuuuuuuuu/basic.git
   cd basic
   ```  
2. **Start the Flask server:**  
   ```bash
   python tracker.py
   ```  
3. **Run Ngrok to create a public link:**  
   ```bash
   ngrok http 5000
   ```  
4. **Share the generated link** and monitor incoming connections.  

## Usage  
- Run the script to generate a tracking link.  
- Anyone who accesses the link will have their IP logged.  
- The collected data will be displayed in the console or stored in a file.  

## Repository  
🔗 **GitHub:** [IP Tracker Repository](https://github.com/anshuuuuuuuuuuuuu/basic/blob/main/README.md)  

## Disclaimer  
This tool is for **educational and security research purposes only**. **Unauthorized tracking is illegal**—use responsibly.  
