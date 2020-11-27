# 크롤링 연습
학교 수강신청 페이지에서 강의명, 교수명, 전공, 강의 구분으로 이루어진 강의 정보를 크롤링한 다음에 장고를 이용해 이를 웹에 보여지게 하는 것을 목표다!!<br/>

## 크롤링하는 방법(간단하게~)
### 1) 웹 페이지에 모든 정보가 나타나는 경우.
   html에 모든 정보가 담겨 있는 경우에는 requests와 BeautifulSoup을 이용해서 크롤링.<br/>

   사용하기 전에  설치하기.<br/>

   '''shell
   pip install requests

   pip install BeautifulSoup
   '''


### 2) 웹 페이지에 모든 정보가 보여지지 않고 이후 사용자의 동작에 따라 js를 이용해 정보를 가져와 보여주는 경우.
   html에 일부만 담겨 있거나 틀만 잡혀있는 경우, requests와 BeautifulSoup만을 가지고는 크롤링이 불가능.<br/><br/>

   selenium이라고 부르는 웹 앱 테스트용 프레임워크의 도움을 받아야 함. selenium은 webdriver라는 API를 통해 운영체제에 설치된 브라우저를 제어해준다고 함.<br/>
   개발자가 작성한 코드대로 브라우저를 열어 해당 url로 이동한 뒤에 코드 내용대로 수행.<br/><br/>

   사용하기 전에 설치하기.<br/>

   '''shell
   pip install selenium
   '''<br/>
   webdriver도 설치해야 함.<br/>
   크롬을 이용해서 크롤링할 것이기 때문에 chromedriver를 설치~~<br/>


   책 '파이썬 코딩 도장' 구글링해서 찾은 여러 블로그 글, 깃허브 wwlee94/everytime-timetable-crawling 참고했음...!<br/>