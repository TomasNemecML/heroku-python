# a-offscreen
from bs4 import BeautifulSoup
import requests

def getPriceAmazon(url):

    headers = {'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254'}

    r = requests.get(f"https://{url}", headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    priceElement = soup.find("span", class_="a-offscreen")
    return soup
    return priceElement