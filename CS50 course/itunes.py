import requests

url = "https://7j0hdiy5ak.execute-api.us-west-2.amazonaws.com/prod/kurts-smarthome-storage-bucket/PersonalHabits"

headers = {
    "x-api-key": "BXuVto1OxV3xcZyO1xRKTabAE9uYdJPm5Ft5Ndss"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
