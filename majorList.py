from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# 크롬 드라이버의 위치
driver = webdriver.Chrome('크롬드라이버 위치')

# 로그인 페이지 가지고 오기
driver.get('https://everytime.kr/login')
driver.implicitly_wait(5)

# 로그인
driver.find_element_by_name('userid').send_keys('아이디')
driver.find_element_by_name('password').send_keys('비밀번호')
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

# 에타 시간표 페이지 가지고 오기
driver.get('https://everytime.kr/timetable')

# 수업 목록에서 검색 클릭
driver.find_element_by_xpath('//*[@id="container"]/ul/li[1]').click()

#팝업창 닫기
sleep(2)
driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()

# 학과명 가지고 오기
driver.find_element_by_xpath('//*[@id="subjects"]/div[1]/a[3]').click()
driver.find_element_by_xpath('//*[@id="subjectCategoryFilter"]/div/ul/li[1]').click()

page = driver.page_source # 전공목록을 가지고 오기 위해 필터링 메뉴에서 전공/영역 -> 전공 클릭 후 페이지 가져오기
soup = BeautifulSoup(page, 'html.parser')

ul = soup.find('ul', {'class':'unfolded'}) # 학과명 목록이 담긴 <ul> 가져오기
mList = [] # 학과명을 담을 리스트

for li in ul.find_all('li'): # <li>를 모두 찾을 때까지 반복해서
    m = li.text # 텍스트를 가지고 와서 / <li>텍스트</li>
    mList.append(m) # mList에 추가

# 가져온 학과명 csv 파일로 저장하기
with open('majorList.csv', 'w', encoding='utf-8') as file:
    file.write('학과명\n')
    for i in mList:
        file.write(i)
        file.write('\n')