import requests
from requests.exceptions import HTTPError
import urllib3

proxies = {
    "http": 'http://127.0.0.1:3128',  # None
    "https": 'http://127.0.0.1:3128',  # None
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url, proxies=proxies, verify=False)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
