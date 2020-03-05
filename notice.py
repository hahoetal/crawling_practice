# 학부학사 공지 제목만 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup

path = '크롬 드라이버 위치'
driver = webdriver.Chrome(path)

# 해당 url로 이동
driver.get('https://www.sungshin.ac.kr/main_kor/11107/subview.do')

# 5초 기다리기
driver.implicitly_wait(5)

# 웹 페이지 가져오기
html = driver.page_source

# html을 파이썬이 이해할 수 있도록 만들기
soup = BeautifulSoup(html, 'html.parser')

# 공지 내용이 담긴 테이블 찾기
table = soup.find('table', {'class': 'artclTable artclHorNum1'}) # class가 artclTable artclHorNum1인 <table>을 찾아 table에 넣기
notice = [] # 공지 제목을 담을 빈 리스트 생성

# 공지 제목만 뽑아서 notice 리스트에 넣기
for tr in table.find_all('tr'): # table 안에 있는 <tr> 태그를 모두 찾을 때까지
    tds = list(tr.find_all('td')) # 찾은 tr 안에 있는 <td> 태그를 모두 찾아서 리스트(tds)로 만들고

    for td in tds: # tds 리스트에서 요소를 하나씩 꺼내 td에 담고
        if td.find('a'): # td 안에 <a> 태그가 있으면
            a = td.find('a')
            title = a.find('strong').text # a 안에 있는 <strong> 태그 텍스트를 title에 넣기 / <strong>텍스트</strong>
            notice.append(title) # title을 notice 리스트에 추가

# 리스트 notice를 csv 파일로 만들기
with open('notice.csv', 'w', encoding='utf-8') as file:
    for n in notice:
        file.write('{0}\n'.format(n))