#리스트
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers)

#인덱싱
print(numbers[0])
print(numbers[4])

#슬라이싱
print(numbers[1:5])
print(numbers[3:])
print(numbers[:5])

#역순 인덱싱, 슬라이싱
print(numbers[-3])
print(numbers[-4:])
print(numbers[:-3])
print(numbers[-5:-2])

#다양한 형태의 값을 저장할 수 있는 리스트
list1 = [10, '김강민', 3.14, [1, 2, 3, 4], 5]

print(list1)
print(list[1])

print(list1[3][1:3])

#연산 사용하기 (+, *)
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1  + list2
print(list3)
 
list4 = list1 * 3
print(list4)

# 리스트, 튜플, 문자열, 딕셔너리 자료형들의 길이(크기) 구해주는 함수 len()
list1_size = len(list1)
list2_size = len(list2)
list3_size = len(list3)
list4_size = len(list4)
print(list1_size)
print(list2_size)
print(list3_size)
print(list4_size)

list1 = [1, 2, 3]

a = 10
print(a)
a = 20
print(a)

list1[0] = 10
list1[1] = 20
list1[2] = 30

print(list1)

del list1[1]
print(list1)

#함수를 사용하는 방법
list1 = [1, 2, 3]
list1.append(4) # 제일 마지막에 추가해라
print(list1)

num1 = list1.pop(1) # 해당 인덱스의 값을 꺼내라
num1 = list1.pop()  # 아무 인덱스를 넣지 않으면 마지막 값을 꺼낸다.
print(list1)
print(num1)

del list1[0] # 해당 인덱스를 찾아서 제거

num1 = list1.remove(3) # 해당 값을 찾아서 제거해라
print(list1)
print(num1)

list1.insert(1, 10)
list1.insert(1, 20)
print(list1)

list1 = [1, 5, 3, 7, 4]
list1.sort() # 정렬
print(list1)

list1.reverse() # 반전 (역순 나열)
print(list1) 

list1.clear() # 리스트를 비워라

list1 = [1, 1, 1, 1, 2, 3, 4, 4, 4]
num1Count = list1.count(1)
print(num1Count)

num2Index = list1.index(1) # 가장 먼저 있는 인덱스
print(num2Index)


list2 = list1.copy() # 깊은 복사 : 주소안에 있는 모든 값 복사
list1.remove(2)
print(list1)
print(list2)

list3 = list1 # 얕은 복사 : 주소만 복사
list1.remove(3) 
print(list3)
print(list3)

list1.extend([8, 8, 8, 8]) # 리스트에 리스트 더하기 
list1 = list1 + [8, 8, 8, 8]
print(list1)

name = '김강민'
age = '29'
address = '부산시 강서구 대저2동'

print(name)
print(age)
print(address)

myname = "김강민"
myName = "김갱민"

print(myname)
print(myName)

num1 = 10
num2 = 20

print(num1)
print(num2)

# 1num = 30 안됨
n1um = 40

num_1 = 50
_num = 60
num = 70

# if, for, while, pass, self 변수명 사용 불가

studentCode = 2022001
student_code = 22200001

studentCode = 0
studentName = ""
studentYear = 0
studentAge = 0
studentAddress = ""

print("학생정보 입력되는 부분")

studentCode = 20220001
studentName = "김강민"
studentYear = 1
studentAge = 17
studentAddress = "부산광역시 강서구 대저2동"

print("학생정보 출력되는 부분")

print(studentCode, studentName, studentYear, studentAge, studentAddress)

# ,를 넣으면 자동으로 한칸 뛰워줌, 형변환이 필요없음
