# 구글 홈페이지에 들어가 검색하기
from selenium  import webdriver

# chrome webdiriver의 위치, windows는 chromedriver.exe, Mac은 chromedriver
path = '크롬 드라이버가 저장된 곳! 절대 경로로 적어주었다.'
driver = webdriver.Chrome(path)

# url에 접근하기
driver.get('https://google.com/')

# 검색어를 입력하는 곳, input의 이름이 'q'이므로 q를 찾아서 그곳에 커서를 두겠다는 의미.
search_box = driver.find_element_by_name('q')
# 커서가 있는 곳에 해당 값을 넣겠다는 의미, 여기서는 검색어...
search_box.send_keys('멋쟁이사자처럼')
# 제출
search_box.submit()