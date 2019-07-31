from time import time
import requests
from requests.exceptions import HTTPError
import urllib3

proxies = {
    "http": 'http://127.0.0.1:3128',  # None
    "https": 'http://127.0.0.1:3128',  # None
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def decorator(number_of_repeats):
    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(number_of_repeats):
                start_time = time()
                print('The begin of wrapper')
                response = func(*args, **kwargs)
                print('The end of wrapper')
                print(f'Running time is {time() - start_time}.')
            return response, func.__name__
        return wrapper
    return actual_decorator


@decorator(10)
def call_request(urls):
    for url in urls:
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


list_url = ['https://api.github.com', 'https://api.github.com/invalid']
print(call_request(list_url))
