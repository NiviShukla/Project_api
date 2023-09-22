import requests

response = requests.get('http://127.0.0.1:8000/drinks')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
