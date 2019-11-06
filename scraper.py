import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.es/gp/product/B07XS4MGQL?pf_rd_p=29e676dc-0c95-4aa0-977c-12e6ad9e2b5b&pf_rd_r=CTE8C60175D2NAVY9671'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").getText()
price = soup.find(id="priceblock_ourprice").getText()

converted_price = price[0:3]

print(converted_price)
print(title.strip())
