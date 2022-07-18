from turtle import st


sss = "안녕\t하세요. \n 김강민\"입니다."
print(sss)

print("=" * 10)

#문자열의 길이 구하기 len()
print(len("가나다라마바사"))

#인덱싱과 슬라이싱
strValue = "abcde"
print(strValue[1:4])

a = 'Pithon'

# 문자열을 리스트로 변환하는 방법
b = list(a)

# 리스트로 바뀐 문자열 1번 인덱스의 값에 y 대입
b[1] = 'y'
print(b)

# 리스트의 모든 값을 하나의 문자열로 합치는 방법
a = ''.join(b) 
print(a)

strValue = '%s님의 나이는 %s입니다.' %("김강민", 17)

print(strValue)

name = "김강민"
age = 17
# 일반적인 표현식을 사용한 문자열 포매팅
strValue1 = '%s님의 나이는 %s입니다.' %(name, age)
print(strValue1)

strValue2 = name + "님의 나이는" + str(age) + "입니다."

print(strValue2)

strValue3 = name, "님의 나이는" , age, "입니다."

print(strValue3)

print(name, "님의 나이는", age, "입니다.")

# 포맷함수를 사용한 문자열 포매팅

strValue = "{0}님의 나이는 {1}입니다.".format("김강민", 17)
print(strValue)

name = "김강민"
age = 17
strValue = "{name}님의 나이는 {age}입니다.".format(name=name, age=age)
print(strValue)

strValue2 = f"{name}님의 나이는 {age}입니다."
print(strValue2) 



strValue = "hello, python"

# 문자열에 해당 문자가 몇개인지 확인하는 함수
print(strValue.count("l"))

jStrValue = "/".join(strValue)
print(jStrValue)

strList = ["100", "200", "300", "400"]
strList2 = [100, 200, 300, 400]

print(";".join(strList))
# strValue2에 들어 있는 정수(int) 자료형의 값들을 문자열로 반환
print(list(map(str, strList2)))
# strList에 들어 있는 문자열(string) 자료형의 값들을 정수로 변환
print(list(map(int, strList)))

# 문자열의 양쪽 끝에 있는 공백 지우기
strValue = " 코리아 아카데미 "
print(strValue.strip())

# 문자열에서 해당 문자열을 찾ㅇ사ㅓ 다른 값으로 바꿔라
strValue2 = "코리아 아카데미"
print(strValue2.replace(" ", ""))
phoneNumber = "010-4893-5476"
print(phoneNumber.replace("-",""))

address = " 부산광역시 강서구 대저동 "
# 부산-동래-사직

address1 = phoneNumber.strip()
address2 = address1.replace(" ", "-")
print(address.strip().replace(" ", "-").replace("광역시", "").replace("구", "").replace("동", ""))

