# ListDict.py
# Set형식
a = {1,2,3,3}
b = {3,4,5,4}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Tuple
tp = (10,20,30)
print(len(tp))

# 함수정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

#형식변환(Type Casting)
a = (1,2,3)
b = list(a)
b.append(a)
print(b)

#딕셔너리
fruits = {"apple":"red", "banana":"yellow"}
print(fruits)
print(fruits["apple"])
#입력
fruits["kiwi"] = "green"
del fruits["apple"]
print(fruits)
print()
#반복문
for item in fruits.items():
    print(item)

