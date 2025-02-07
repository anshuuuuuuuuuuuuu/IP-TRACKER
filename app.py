from flask import Flask, request
import requests

app = Flask(__name__)

# Your Flask application setup

@app.route('/track')
def track():
    # Get the user_id from the query parameters
    user_id = request.args.get('user_id')
    
    # Use Ipify API to get the user's public IP address
    ipify_url = 'https://api.ipify.org?format=json'
    try:
        response = requests.get(ipify_url)
        ip_data = response.json()
        user_ip = ip_data.get('ip', 'Unknown IP')
    except requests.exceptions.RequestException as e:
        user_ip = 'Unable to retrieve IP'
    
    # Use Ipinfo.io API to get geolocation information based on IP
    ipinfo_url = f'https://ipinfo.io/{user_ip}/json'
    try:
        geo_response = requests.get(ipinfo_url)
        geo_data = geo_response.json()
        print(geo_data)  # Print the full geolocation response for debugging
        
        # Extract geolocation details
        country = geo_data.get('country', 'Unknown Country')
        city = geo_data.get('city', 'Unknown City')
        region = geo_data.get('region', 'Unknown Region')
    except requests.exceptions.RequestException as e:
        country = city = region = 'Unable to retrieve geolocation data'
    
    # Print the details (user_id, IP, geolocation) in the terminal for debugging
    print(f"User ID: {user_id} - IP Address: {user_ip} - Location: {city}, {region}, {country}")
    
    # Respond back to the user with the tracking data
    return f"Tracking data: User ID: {user_id}, IP Address: {user_ip}, Location: {city}, {region}, {country}"

if __name__ == '__main__':
    app.run(debug=True)
