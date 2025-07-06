import requests

url = "http://127.0.0.1:5000/calc"
payload = {
    "a": 7,
    "b": 3,
    "operation": "*"
}

response = requests.post(url, json=payload)
print("Status code:", response.status_code)
print("JSON response:", response.json())