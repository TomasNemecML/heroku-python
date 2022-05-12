import requests
from bs4 import BeautifulSoup
from lxml import etree

def bestPrice(productID):

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}

    r = requests.get(f"https://www.google.com/search?q={productID}+site%3Aalza.sk", headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    # firstProductPage = soup.find("div", class_="yuRUbf")
    # firstLink = firstProductPage.find("a")
    dom = etree.HTML(str(soup))
    firstLink = dom.xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div/a')

    print(firstLink[0])
    # return firstLink[0]["href"]
    return "123"