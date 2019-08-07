from urllib.parse import urljoin, urlsplit

import requests
import lxml.html


DOMAIN = 'http://python.org'
NETLOC = urlsplit(DOMAIN).netloc

MAX_PAGES = 10

queue = [DOMAIN]  # threading.Queue
visited = set()


with requests.Session() as session:
    count_visited = 0

    while True:
        if count_visited > MAX_PAGES:
            break
        url = queue.pop()
        print(url)
        count_visited += 1
        res = session.get(url)  # blocking
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
