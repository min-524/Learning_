# 부울 연산 
# True = 1, False = 0
# and(&) - 곱
# 1  and  1 => 1
# 1  and  0 -> 0
# 0  and  0 -> 0 


from re import M


print(True and True)
print(True and False)
print(False and False)
print("=" * 30)

# or(|) - 합
# 1 or 1 -> 1
# 1 or 0 -> 1
# 0 or 0 -> 0
print(True or True)
print(True or False)
print(False or False)
print("=" * 30)

# not(!) - 부정
# not True => False
# not False => True
print(not True)
print(not False)

# 대입 연산자
name = "김강민"

# 부호 연산자
num = 1
num = -1

# 산술 연산자
result = 10 + 2
result = 10 - 2
result = 10 * 2
result = 10 ** 2 # 제곱
result = 10 / 2
result = 10 // 2 # 몫
result = 10 % 2 # 나머지 

# 비교 연산자
print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

# 논리 연산자
print(True and False)
print(True or False)
print(not (True or True))

# 복합대입 연산자
num = 10
num += 5
num %= 5

# 삼항(조건) 연산자
result = 0 if 10 > 5 else 1 


membership = "vip"
year = 5
if membership == "vip" and year > 4:
    print("이벤트에 참여가능합니다.")
    print(f"등급: {membership}")
    print(f"년차:{year}년")
    print(f"등급: {membership}\n년차: {year}년")
    print(f"""등급: {membership}
          년차: {year}년""")