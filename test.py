from hashlib import new
import requests
from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlopen
from urllib.parse import quote_plus


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# main
if __name__ == "__main__":
    inputURL = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259"
    response = requests.get(inputURL, headers=headers)
    beautifulSoup = BeautifulSoup(response.content, "html.parser")
    new_text = beautifulSoup.find("ul", attrs={"class":"type06_headline"}).get_text()

    new_img = new_text.find("img")
    attr = beautifulSoup.select_one("ul > li > dl > dt > a > img")
    print(new_text)
    print(new_img["src"])
    



