dan = 2
num = 0

# while dan < 9:
#     num = 0
#     print(f"{dan}단")
#     while num < 9:
#         num += 1
#         print(f"{dan} X {num} = {dan*num}", end="\t")
#     dan += 1
#     print("")
    
# year = "2022"
# month = "07"
# day = "15"
# hour = "16"
# minute = "42"
# second = "30"
# print(year, month, day, sep="/", end=" ")
# print(hour, minute, second, sep=":")

# list1 = list(range(1, 11))
# list2 = [i * 2 for i in list1]
# print(list1)
# print(list2)

# list3 = [i * 3 for i in list1 if i % 3 == 0]
# print(list3)

# list4 = [ i * j for i in list2 for j in list3]
# print(list4)

# list1 = list(range(1,11))
# i = 0

# while i < len(list1):
#     if i % 2 == 0 and i != 0:
#         i+=1
#         break
#         #continue
#     print(list1[i])
#     i += 1
    
# for i in list1:
#     if i % 2 == 0 :
#         continue
#     print(i)
    
# # 함수 

# def add(a, b, c):
#     print(f"a:{a}")
#     if a == 10:
#         return
#     print(f"b:{b}")
#     print()
#     return a + b - c

# result = add(10, 20, 30)
# print(f"result : {result}")

def breakAndReturn(list1):
    for num in list1:
        if num == 5:
            break
        print(num)
    print("함수 끝까지 실행됨.")

numList = list(range(1, 11))

breakAndReturn(numList)

def passTest():
    pass 

if 10 > 5:
    pass

passTest()

