import requests
r = requests.get('https://api.github.com/events')
print(r.status_code)
if r:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {r.status_code}")