# selenium 이용해서 스크롤하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 입력 이벤트 발생시키기
from selenium.webdriver.common.action_chains import ActionChains # actionchain 사용하기

path = '크롬 웹드라이버 경로'
driver = webdriver.Chrome(path)

# driver.get('https://www.naver.com/')

# element1 = driver.find_element_by_css_selector(
#     '#footer > div > div.notice_area > div > h3 > a'
# )

# 1) 내장함수 이용.
# location = element1.location_once_scrolled_into_view

# print(location)
# output: {'x': 30, 'y': 425}

# 2) script 실행/ driver.execute_script('스크립트', element)
# driver.execute_script('arguments[0].scrollIntoView(true);', element1)

# 3) Keys를 활용_키보드 입력 이벤트 발생
# element2 = driver.find_element_by_tag_name('body')
# element2.send_keys(Keys.PAGE_DOWN) # 끝까지 내려가지는 않고 살짝...

# 4) ActionChains
# 네이버 웹툰 페이지에 들어가서 웹툰 웹소설 온라인 광고 판권 사업 홍보 페이지 클릭 
driver.get('https://comic.naver.com/index.nhn')

element3 = driver.find_element_by_xpath(
    '//*[@id="aside"]/div[7]/a/img'
    )
actions = ActionChains(driver).move_to_element(element3).click()
actions.perform() # action 실행

# 참고 사이트
# https://jhleeeme.github.io/scrolling-in-selenium/