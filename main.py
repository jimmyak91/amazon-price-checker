from bs4 import BeautifulSoup
import requests, lxml, smtplib

AMZ_URL = "https://www.amazon.com.au/EVO-Interface-production-audio-interface-microphone/dp/B084BGC5LR/?th=1"
TARGET_PRICE = 165
SOURCE_EMAIL = "jimmyak.test@gmail.com"
SOURCE_EMAIL_PW = ""
TARGET_EMAIL ="james.a.keech@gmail.com"


# Get amazon webpage html
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(AMZ_URL, headers=header)
data = response.text


soup = BeautifulSoup(data, "lxml")
price_html = soup.find(name="span", class_="a-offscreen")
current_price = float(price_html.getText().replace("$", ""))

if current_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connect:
         connect.starttls()
         connect.login(user=SOURCE_EMAIL, password=SOURCE_EMAIL_PW)
         connect.sendmail(from_addr=SOURCE_EMAIL,
                          to_addrs=TARGET_EMAIL,
                          msg=f"Subject: Price Alert - EVO 4 USB Audio Interface!\n\n"
                              f"The price for the EVO 4 USB Audio Interface has dropped below ${TARGET_PRICE}!\n\n"
                              f"The current price is ${current_price}\n"
                              f"Click this link to purchase - {AMZ_URL}")
