## 강의 정보 가지고 오기
from selenium import webdriver
from bs4 import BeautifulSoup # 가지고 온 html을 파싱하여 python이 이해할 수 있게 해주는 모듈
from selenium.webdriver.support.ui import Select # html에서 select의 option 선택을 위해서 추가

# chromedriver 위치 지정
path = '크롬 드라이버의 위치'
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

driver.find_element_by_id('id').send_keys(user)
driver.find_element_by_id('password').send_keys(pw)
driver.find_element_by_id('submit').click()
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

    lectureName = professor = major = separation = ''

    for n in range(len(tds)): # tds의 길이만큼 반복
        if n == 1:
            major = tds[1].text
        elif n == 3:
            lectureName = tds[3].text
        elif n== 5:
            separation = tds[5].text
        elif n == 13:
            professor = tds[13].text
        else:
            pass # n이 1, 3, 5, 13이 아닌 경우에는 아무 것도 수행하지 않고 넘어감.     
            
    lecture.append([lectureName, professor, major, separation])


# 가지고 온 데이터를 csv 파일로 만들기
with open('lecture.csv', 'w', encoding='utf-8') as file:
    file.write('lectureName, professor, major, separation\n')
    for i in lecture:
        file.write('{0},{1},{2},{3}\n'.format(i[0], i[1], i[2], i[3]))

# 동일한 강의를 반을 나누어서 수업하는 경우, 강의 시간과 대상자만 다를 뿐 모든 것이 동일하다.
# 이것까지 고려해서 크롤링하는 건... 지금 생각하기에 불가능한 것 같다.