import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver") # 웹드라이버 파일의 경로
driver.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259")
time.sleep(5) # 5초동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, "html.parser")

thumbnails = soup.select(".photo > a > img")
#크롬에서 가져오고 싶은 이미지의 태그를 선택해서 copy selecotr로 가져옴


i=1
for thumbnail in thumbnails: # 해당페이지의 이미지들의 태그들을 모두 가져옴
    src = thumbnail["src"]   # 가져온 태그 정보중에 src만 가져옴
    dload.save(src,f'imgs/{i}.jpg')   # 설정한 경로로 jpg 파일로 다운로드함
    i+=1
  
driver.quit()

