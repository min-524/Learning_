from sys import stderr


strTuple = (1, 2, 3, 4, 5)
strList = [1, 2, 3, 4, 5]

strList[2] = 30 
print(strList)

# strTuple[2] = 30
print(strTuple)

num = 10
num = 20

strTuple = (1, 2, 3)
print(type(strTuple))
print(type(strList))

strList = [1]
strTuple = (1,)

print(type(strTuple))
print(type(strList))


# 딕셔너리 
strDict = {"이름": "김강민", "나이": 17}
print(strDict)

print(type(strDict["이름"]))
print(type(strDict["나이"]))

strDict["주소"] = "부산 강서구"
print(strDict)

strDict["나이"] = 30
print(strDict)

del strDict["주소"]
print(strDict)

# 리스트를 Key로 사용할 수 없는 이유

strDict = {1:10, "김": "김강민"}
print(strDict[1])
print(strDict["김"])

strDict = {"이름" : "김강민", "나이" : 17}

# key 값만 리스토로 추출
print(strDict.keys())
KeyList = list(strDict.keys())

# value값만 리스트로 추출
print(strDict.values())
ValueList = list(strDict.values())

# key와 value값만 리스트로 추출
print(strDict.items())
itemList = list(strDict.items())

# strDict.clear()
print(strDict)

print(strDict["이름"])
print(strDict.get("이름"))

strDict.update({"이름" : "김갱민"})
print(strDict)

strDict.update({"주소" : "부산"})
print(strDict)

print(strDict.popitem())

strSet = set([1, 2, 3, 4])
print(strSet)

a = {}
print(type(a))

b = set()
print(type(b))

print(a, b)

s1 = set("hello, python")
s2 = set("hello, java")
s3 = set("javajavaaa")

print(s1)
print(s3)

# 교집합
r1 = s1 & s2 
print(r1)
r1 = s1.intersection(s2)
print(r1)

# 합집합
r2 = s1 | s2 
print(r2)
r2 = r1.union(s2)

# 차집합
r3 = s1 - s2
print(r3)
r3 = s2 -s1
print(r3)
r3 = s1.difference(s2)
print(r3)
r3 = s2.difference(s1)
print(r3)

s1 = set([10, 20, 30, 40])

# 값 추가
s1.add(50)
print(s1)

# 값을 여러개 한번에 추가
s1.update([50, 60, 70, 70])
print(s1)

# 값을 해당 값을 선택 제거
s1.remove(10)
print(s1)

# 정렬된 set의 앞쪽부터 값을 하나씩 꺼냄
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
