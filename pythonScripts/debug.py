import requests
from bs4 import BeautifulSoup


def getPage(url):

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}

    r = requests.get(f"https://{url}", headers=headers)
    # soup = BeautifulSoup(r.text, "html.parser")
    return r.text