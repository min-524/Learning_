treeHit = 0

while treeHit < 10 : 
    treeHit += 1
    print(f"너무를 {treeHit}번 찍습니다.")
    if treeHit == 10 :
        print("나무가 쓰러집니다")
        
i = 0
while i < 10:
    print(i)
    i += 1
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
 
# name = input("이름을 입력하세요 : ")
# age = input("나이를 입력하세요 : ")
# address = input("주소를 입력하세요 : ")

# content = f"""
# 이름 : {name}
# 나이 : {age}
# 주소 : {address}
# """
# print(content)

# a = 10
# b = 20
# c = 30
# print(f"결과 : {a + b + c}")

# a, b, c = [1, 2, 3]
# print(a, b, c)

# arr = "10 20 30".split()
# print(arr)
# print(list(map(int, arr)))

# numbers = input("숫자 3개 입력 : ")
# print(list(map(int, numbers.split())))
# a, b, c = map(int, numbers.split())
# print(f"{a}, {b}, {c}")

# a, b, c = map(int, input("숫자 3개 입력 : ").split())
# print(a + b + c)

dan = 2 
num = 0

# 구구단
while dan < 9:
    num = 0
    print(f"{dan}단")
    while num < 9:
        num += 1
        print(f"{dan} X {num} = {dan*num}")
    dan += 1
    
i = 0

while i < 5:
    j = 0 
    while j < 3:
        k = 0
        while k < 2:
            print(f"i[{i}], j[{j}], k[{k}]")
            k += 1
        j += 1
    i += 1
    
for i  in [1, 2, 3, 4, 5]:
    print(i)
    
a, b, c = [1, 2, 3]
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(f"i[{i}]")
    print(f"j[{j}]")

scoreList = [69, 39, 50, 60, 70]
num = 0 
for score in scoreList:
    num += 1
    print(f"{num}번 학생의 점수는 {score}입니다.")
    if score > 59:
        print("합격")
    else:
        print("불합격")
        
num = 0
 
for score in scoreList:
    num += 1
    print(f"{num}번 학생의 점수는 {score}입니다")
    if score > 59:
        print("합격")
    else:
        print("불합격")
        