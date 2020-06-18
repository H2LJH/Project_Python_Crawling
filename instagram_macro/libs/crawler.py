import requests


def crawl(url):
    resp = requests.get(url)
    print(resp, url)
    return resp.content