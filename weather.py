import requests # 웹 페이지의 html 가지고 오는 모듈
from bs4 import BeautifulSoup # 가지고 온 html을 파싱하여 python이 이해할 수 있게 해주는 모듈

response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html') # 해당 url의 웹 페이지 가져오기
soup = BeautifulSoup(response.content, 'html.parser') # 가지고 온 웹 페이지(html)를 html.parser를 이용해 BeautifulSoup 객체로 만듦

table = soup.find('table', {'class': 'table_develop3'}) # 가지고 오고 싶은 데이터를 찾기 / <table class="table_develop3"> 찾기
data = [] # 원하는 데이터를 담을 리스트

for tr in table.find_all('tr'): # 모든 <tr>을 찾아서 반복!
    tds = list(tr.find_all('td')) # 찾은 <tr>의 모든 <td>를 찾아서 리스트로 만들기 / [<td><a href=---->서울</a></td>, <td>----</td>, ...]

    for td in tds: # <td>들로 구성된 리스트의 요소를 하나씩 꺼내가면서..
        if td.find('a'): # <td>로 이루어진 리스트 안에 <a>를 찾으면
            point = td.find('a').text # <a>를 찾아서 태그 안에 있는 텍스트 가져와 point에 넣기 / <a>텍스트</a>
            temperature = tds[5].text # 리스트 tds의 5번 인덱스 요소인 td 태그 사이에 있는 텍스트를 temperature에 넣기
            humidity = tds[9].text # 리스트 tds의 10번째 요소의 텍스트 humidity에 넣기
            data.append([point, temperature, humidity]) # 데이터들을 리스트로 만들어 빈 리스트인 data에 추가! / 중복리스트~

print(data)


with open('weather.csv', 'w', encoding='utf-8') as file: # weather.csv을 쓰기 모드로 열고 encoding 방식은 utf-8로 지정
    file.write('point, temperature, humidity\n') # 칼럼에 이름 추가
    for i in data:
        file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2])) # 지점, 온도, 습도를 줄 단위로 저장

# 한글이 깨져서 csv 파일이 만들어짐
# with open('weather.csv', 'w') as file: 
#    file.write('point, temperature, humidity\n') 
#    for i in data:
#        file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2])) 


# 파이썬 코딩 도장 참고 해서 작성!!