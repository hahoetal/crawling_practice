# 이미지 크롤링
# urllib 패키지: URL을 통해 여러 작업을 수행하는 모듈들의 패키지
# urllib.request: HTTP 요청 기능을 담은 모듈.
# urllib.parse: URL 해석 및 조작 기능을 담은 모듈.

from urllib.request import urlopen # URL을 여는 함수, 웹 서버에 정보를 요청한 다음, 돌려받은 응답을 저장하여 HTTPResponse를 반환.
from urllib.parse import quote_plus # url에 한글이 포함되면 오류가 나기 때문에 한글을 유니코드로 변환해야 함.
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요: ')
crawl_num = int(input('크롤링할 개수를 입력하세요: '))
url = baseUrl + quote_plus(plusUrl) # 유니코드로 변환된 한글을 포함한 url 

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all('img', {'class':'_img'}) # class가 '_img'인 <img> 태그를 모두 찾아서 img에 할당.

n = 1
for i in img:
    imgUrl = (i['data-source']) # <img> 태그의 src, 즉 이미지 url 값을 가져와 imgUrl에 할당.

    with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h: # img 폴더 안에 검색어 + 번호.jpg로 이미지 저장, wb binary 모드로 파일 작성.
        img = urlopen(imgUrl).read()
        h.write(img)
            
    n += 1

    if n > crawl_num:
        break

print('다운로드 완료')