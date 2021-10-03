from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.sg/Fisher-Price-Imaginext-SpongeBob-Preschool-Exclusive/dp/B07P98B1WD/'

result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
price = doc.find("span", {"id": "priceblock_ourprice"})
title = doc.find("span", {"id": "productTitle"})
print(title.string,price.string)
