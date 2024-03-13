# web2.py
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "html.parser")
f = open("dangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n", "").strip()
    price = priceElem.text.replace("\n", "").strip()
    addr = addrElem.text.replace("\n", "").strip()
    # print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close()


# <div class="card-desc">
#   <h2 class="card-title">아이폰13pro</h2>
#   <div class="card-price ">
#     300,000원
#   </div>
#   <div class="card-region-name">
#     부산 북구 만덕제2동
#   </div>