import json
import requests

response = requests.get("https://musicbrainz.org/ws/2/release?artist=65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab&status=bootleg&type=live")
if response.status_code == 200: 
    headers = response.headers
    text = response.text

    print(text)
else:
    print("Error")