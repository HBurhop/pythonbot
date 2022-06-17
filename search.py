import requests
import random
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
URL = "https://www.mindfactory.de/product_info.php/8GB-MSI-GeForce-RTX-3070-GAMING-X-TRIO-DDR6_1381128.html"
URL2 = "https://www.mindfactory.de/Hersteller_Shops/MSI_Shop/Hardware/Grafikkarten+(VGA)/GeForce+RTX+fuer+Gaming.html/referrer/category"
URL3 = "https://www.amazon.de/dp/B08HM4V2DH"
while True:
    page = requests.get(URL, headers=headers)
    page2 = requests.get(URL2, headers=headers)
    page3 = requests.get(URL2, headers=headers)
    status_code = page.status_code
    content = BeautifulSoup(page2.content, "html.parser")
    content2 = BeautifulSoup(page3.content, "html.parser")
    soup = BeautifulSoup(page.content, "html.parser")
    random_number = random.randint(4, 9) * 60
    toaster = ToastNotifier()
    preis = soup.find(id="not_available_anymore")
    print(random_number)
    if content2.find(id="desktop_unifiedPrice"):
        continue
    elif page3.status_code == 404:
        toaster.show_toast("Amazon Fehler", "Guck bei Amazon")
    elif content2.find(id="priceblock_ourprice"):
        toaster.show_toast("Amazon checken!", "AMAZON")
    if not preis:
        time.sleep(random_number)
    elif preis:
        toaster.show_toast("RTX Kaufen Mindfactory", "Mindfactory")
        break
    else:
        toaster.show_toast("Irgendein Fehler guck nach!", "Mindfactory")
        break
