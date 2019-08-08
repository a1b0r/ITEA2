# Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор.
# Создать список из 10 ссылок, по которым будет происходить скачивание. Создать список потоков, отдельный поток,
# на каждую из ссылок. Каждый поток должен сигнализировать, о том, что, он начал работу и по какой ссылке он работает,
# так же должен сообщать когда скачивание закончится.

from urllib.parse import urljoin, urlsplit
import requests
import lxml.html
from threading import Thread
import random
import time


class ThreadGenerator(Thread):
    def __init__(self, name):
        self._name = name
        Thread.__init__(self, name=self._name)

    def run(self):
        print(f"I'm executing Thread with link {self._name}")
        time.sleep(random.randint(0, 5))
        print(f"The end with link {self._name}")


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


DOMAIN = 'http://python.org'
NETLOC = urlsplit(DOMAIN).netloc

MAX_PAGES = 10

queue = [DOMAIN]
visited = set()


with requests.Session() as session:
    count_visited = 0

    while True:
        if count_visited > MAX_PAGES:
            break
        url = queue.pop()
        count_visited += 1
        res = session.get(url)
        if res.status_code == requests.codes.ok:
            try:
                doc = lxml.html.fromstring(res.text)
            except Exception as e:
                print(f'Error {url}: ', e)
            for elem, attr, link, _ in doc.iterlinks():
                link = urljoin(DOMAIN, link)
                if not urlsplit(link).netloc == NETLOC:
                    continue
                if elem.tag == 'a' and attr == 'href':
                    if link not in visited:
                        queue.append(link)
                        visited.add(url)
        else:
            print(f'Invalid url {url}')


@decorator
def run(visits):
    for visit in visits:
        ThreadGenerator(visit).start()


run(list(visited))
