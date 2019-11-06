import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.es/gp/product/B07XS4MGQL?pf_rd_p=29e676dc-0c95-4aa0-977c-12e6ad9e2b5b&pf_rd_r=CTE8C60175D2NAVY9671'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()
    converted_price = float(price[0:3])

    if(converted_price < 800):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pruebasmanueldev@gmail.com', 'yalasabes99-')

    subject = 'Price fell down'
    body = 'Check the amazon link! https://www.amazon.es/gp/product/B07XS4MGQL?pf_rd_p=29e676dc-0c95-4aa0-977c-12e6ad9e2b5b&pf_rd_r=CTE8C60175D2NAVY9671'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pruebasmanueldev@gmail.com',
        'manuelbalbas@gmail.com',
        msg
    )
    print('Hey! Email has been sent!!')


check_price()
