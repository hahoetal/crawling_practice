# 에브리타임에서 시간표 크롤링하기
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome('C:/Users/yeong/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://everytime.kr/login')
# 암묵적으로 웹 자원 로드를 위해 5초까지 기다리기
driver.implicitly_wait(5)

# 로그인.
driver.find_element_by_name('userid').send_keys('아이디')
driver.find_element_by_name('password').send_keys('비밀번호')
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

# 에타 시간표 페이지
driver.get('https://everytime.kr/timetable')

#수업 목록에서 검색 클릭
driver.find_element_by_xpath('//*[@id="container"]/ul/li[1]').click()

#팝업창 닫기
sleep(2)
driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()

# 전공 선택
driver.find_element_by_xpath('//*[@id="subjects"]/div[1]/a[3]').click() # 필터링 메뉴에서 '전공/영역' 클릭
driver.find_element_by_xpath('//*[@id="subjectCategoryFilter"]/div/ul/li[1]').click() # 전공 클릭
driver.find_element_by_xpath('//*[@id="subjectCategoryFilter"]/div/ul/ul[1]/li[10]').click() # 원하는 전공 선택
    
pre_count = 0
#스크롤 맨아래로 내리기
while True:
    #tr요소 접근
    element = driver.find_elements_by_css_selector("#subjects > div.list > table > tbody > tr")

    # tr 마지막 요소 접근
    result = element[-1]
    # 마지막요소에 focus주기
    driver.execute_script('arguments[0].scrollIntoView(true);',result)
    sleep(2)

    # 현재 접근한 요소의 갯수
    current_count = len(element)
    if pre_count == current_count:
        break
    #같지않다면
    pre_count = current_count


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#subjects > div.list > table > tbody > tr')

results = []

for tr in trs:
    result=[]
    tds = tr.select('#subjects > div.list > table > tbody > tr > td')
    result.append(tds[3].text) # 강의명
    result.append(tds[4].text) # 교수
    result.append() # 과 이름
    result.append() # 구분
    results.append(result)


# 값이 들어있다면!
#if results:
#    print(results)

with open('lecture.csv', 'w', encoding='utf-8') as file:
    file.write('강의명, 교수, 학과명, 구분\n')
    for i in results:
        file.write('{0},{1},{2},{3}\n'.format(i[0], i[1], i[2], i[3]))