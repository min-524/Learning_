# Korea IT 세번째 강의

### 이스케이프 문자
<ul>
    <li> \t = 탭(Tab)
    <li> \n = 라인피드(Linefeed) -> 줄바꿈
    <li> \r = 캐리지(Carriage Return)
    <li> \\ = 역슬래시 (Backslash)
    <li> \' = 작은 따옴표 (Single Quote)
    <li> \" =  큰 따옴표 (Double Quote)
</ul>

count("x") -> 문자열에 x가 몇개인가 확인하는 함수
find('x') -> 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환
index('x') -> 오류가 나면 프로그램이 멈춤
"asd".join('123') -> 123사이사이에 asd를 넣는다
upper -> 소문자를 대문자로
lower -> 대문자를 소문자로
lstrip -> 왼쪽 공백 지우기
rstrip -> 오른쪽 공백 지우기
strip -> 양쪽 공백 지우기
replace(" ", "") -> 중간 공백 지우기
split -> 문자열 나누기
