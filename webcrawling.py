# 네이버 뉴스 가져오기
# 헤드라인 뉴스에서 가장 위에 있는 뉴스의 기사!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

path = "크롬 드라이버가 저장된 위치, 절대 경로로 적어주었다."
driver = webdriver.Chrome(path)
driver.get("https://www.naver.com/")

a = driver.find_elements_by_xpath('//*[@id="PM_ID_serviceNavi"]/li[2]/a') # driver.find_elements_by_xpath('크롬 개발자 도구에서 copy -> copy XPath안 값')
# 여기서 a는 list 상태가 됨...
driver.get(a[0].get_attribute('href'))
# elements 안에 있는 href 속성 값으로 web driver가 접속하게 됨.
# 클릭하지 않았지만 클릭한 것 같은....

b = driver.find_elements_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a')
driver.get(b[0].get_attribute('href'))

req = driver.page_source # web driver가 현재 실행 중인 웹 사이트의 소스를 가져오기 위함
soup = BeautifulSoup(req, 'html.parser') # 가지고 온 웹 페이지(html)을 html.parser를 이용해서 BeautifulSoup 객체로 만듦

news = soup.select('#articleBodyContents')

for n in news:
    print(n.text)