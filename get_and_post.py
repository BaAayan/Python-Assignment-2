import requests

# GET request (for comparison)
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},     # becomes ?userId=1 in the URL
    timeout=10,
)
print(response.status_code)   # 200
print(len(response.json()))

# POST request sending JSON data
url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Term 3 Notice",
    "body": "School fees are due on Friday.",
    "userId": 1,
}
headers = {"Accept": "application/json"}

try:
    # json= serialises the dictionary and sets Content-Type: application/json
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()   # raises an error for 4xx / 5xx responses

    print("Status code:", response.status_code)   # 201 Created
    print("Response   :", response.json())

except requests.exceptions.HTTPError as err:
    print("The server returned an error:", err)
except requests.exceptions.RequestException as err:
    print("The request failed:", err)

# POST request sending form-encoded data
response = requests.post(
    "https://example.com/login",
    data={"username": "paul", "password": "secret"},
    timeout=10,
)