import requests

# Send HTTP GET request (request.get('url')) and return an object containing the response.
response = requests.get('http://aosabook.org/en/500L/web-server/testpage.html')

print(f'Status Code: {response.status_code}')
print(f'Content Length: {response.headers['content-length']}')
print(f'Body: \n{response.text}')