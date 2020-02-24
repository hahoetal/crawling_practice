# 네이버 로그인
# 자동 로그인 방지가 떠서 로그인이 중간에 막히지만 그 전 단계까지는 감.

from selenium import webdriver
# 컴퓨터 자판에 있는 키를 입력한 것과 같은 효과를 주기 위해 가져온 모듈
from selenium.webdriver.common.keys import Keys # 이 부분을 주석 처리하고 파일을 실행하면, login.send_keys(Keys.RETURN) 코드 작동 안 됨.

# 자동 로그인을 위해... 아이디와 비밀번호를 작성
user = '아이디'
pwd = '비밀번호'

# 사용할 웹 드라이버의 위치(경로) 저장
path = '크롬 드라이버가 저장된 위치, 절대 경로로 적어주었다.'
# 해당 경로에 있는 chromewebdriver를 가져와 driver에 넣기
driver = webdriver.Chrome(path)

# 해당 url에 접근, 네이버 로그인 창으로 바로 이동
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

login = driver.find_element_by_id('id') # id가 id인 곳을 찾아 커서를 두고
login.send_keys(user) # user 값을 커서가 있는 곳에 넣고
login = driver.find_element_by_id('pw') # id가 pw인 곳을 찾아서 커서를 두고
login.send_keys(pwd) # pwd 값을 커서가 있는 곳에 넣고
login.send_keys(Keys.RETURN) # Enter 키 누르기

# 일단 로그인이 막힘 없어 되었다고 치고 로그아웃 코드 작성해보기
#logout = driver.find_element_by_id('btn_logout') # id가 btn_logout인 곳에 커서를 두고
#logout.send_keys(keys.RETURN) # Enter 키 누르기
# 이렇게 작성하면 로그인 한 다음에 로그아웃도 될 것 같은데... 자동 로그인이 중간에 멈춰서 확인은 못했다.
