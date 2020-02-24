## 강의 정보 가지고 오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests # 웹 페이지의 html 가지고 오는 모듈
from bs4 import BeautifulSoup # 가지고 온 html을 파싱하여 python이 이해할 수 있게 해주는 모듈
from time import sleep
from selenium.webdriver.support.ui import Select # html에서 select의 option 선택을 위해서 추가

# chromedriver 위치 지정
path = '크롬 드라이버가 저장된 위치, 절대 경로로 적어주었다.'
driver = webdriver.Chrome(path)

# 수강신청 페이지 아이디와 비밀번호
user = '학번'
pw = '비밀번호'

# url에 접근
driver.get('https://sugang.sungshin.ac.kr')
# 암묵적으로 웹 자원 로드를 위해 7초까지 기다려준다.
driver.implicitly_wait(7)

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="loginLink"]').click()

login = driver.find_element_by_id('id')
login.send_keys(user)
login = driver.find_element_by_id('password')
login.send_keys(pw)
login.send_keys(Keys.RETURN)
# 여기까지 로그인!!

# 개설강좌조회 버튼 클릭
driver.find_element_by_xpath('//*[@id="Smenu"]/ul/li[5]/a').click()
driver.implicitly_wait(3)

# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element...
# xpath, id 등등 여러 메서드를 사용해보고 제대로 경로? 위치를 찾아 넣었음에도
# 대충 위와 같은 오류가 뜬다면 찾는 element가 iframe 안에 있는지 확인해보기

# 조직 분류 선택
# iframe 안에 찾고자 하는 element가 있으므로 frame 바꾸어주기
frame = driver.find_element_by_xpath('//*[@id="contentsFrm"]')
driver.switch_to.frame(frame) 

# 대학에서 열리는 강의를 조회하고 싶으니 '대학'을 선택
org = driver.find_element_by_id('cmbOrgClsfCd')
selectorO = Select(org)
selectorO.select_by_value('COMM075.101')

# 대상과정 선택, '학사과정 선택'
who = driver.find_element_by_id('cmbObjCrsCd')
selectorW = Select(who)
selectorW.select_by_value('USSR001.10')

# 조회 버튼 누르기
driver.find_element_by_xpath('//*[@id="btnSch"]').click()

# 암묵적으로 웹 자원 로드를 위해 기다려주기
driver.implicitly_wait(10)
# 왠지 모르겠지만 아래 코드가 없으면... 강의 목록이 담긴 table을 가지고 올 수 없다.
driver.find_element_by_xpath('//*[@id="grxMst"]/tbody/tr[2]')

html = driver.page_source

# 가지고 온 html에 원하는 정보가 있는지 확인 
#print(html)

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id':'grxMst'})
lecture = [] # 강의 정보를 담을 리스트

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            lectureName = tds[3].text
            professor = tds[13].text
            major = tds[1].text
            separation = tds[5].text
            lecture.append([lectureName, professor, major, separation])


with open('lecture.csv', 'w', encoding='utf-8') as file:
    file.write('lectureName, professor, major, separation\n')
    for i in lecture:
        file.write('{0},{1},{2},{3}\n'.format(i[0], i[1], i[2], i[3]))

# 강의 목록을 가지고 오기는 하지만 파일을 열어서 보면 강의 목록이 똑같은게 두 개씩 있고 그런다.
# 나중에 천천히 보면서 찾아볼 것!!