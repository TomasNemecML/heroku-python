from bs4 import BeautifulSoup
import requests

def getPrice(url, className, tag):

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}

    r = requests.get(f"https://{url}", headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    priceElement = soup.find_all(tag, class_ = className)
    # return soup
    return priceElement[0].text
