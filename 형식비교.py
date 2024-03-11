# 형식비교
# 리스트(List)
my_list = [1, 2, 3, 4, 5]

# 튜플(Tuple)
my_tuple = (1, 2, 3, 4, 5)

# 세트(Set)
my_set = {1, 2, 3, 4, 5}

# 딕셔너리(Dictionary)
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 각 자료형의 타입 확인
print("List 타입:", type(my_list))
print("Tuple 타입:", type(my_tuple))
print("Set 타입:", type(my_set))
print("Dictionary 타입:", type(my_dict))

# 각 자료형의 길이 확인
print("List 길이:", len(my_list))
print("Tuple 길이:", len(my_tuple))
print("Set 길이:", len(my_set))
print("Dictionary 길이:", len(my_dict))

# 요소 추가 및 제거 (리스트, 튜플, 세트는 변경 가능하며, 딕셔너리는 키-값 쌍을 추가 및 제거할 수 있음)
my_list.append(6)
# my_tuple.append(6)  # 튜플은 변경 불가능하여 추가할 수 없음
my_set.add(6)
my_dict['f'] = 6

# 변경 후 각 자료형 출력
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
