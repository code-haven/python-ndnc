import requests

def httpCall():
    url = 'http://google.com'
    response = requests.get(url)
    return response.status_code

