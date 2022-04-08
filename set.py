# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"안효섭", "이도현", "김민규"}
python = set(["안효섭", "송강"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("옹성우")
print(python)

# java를 잊었어요
java.remove("김민규")
print(java)


# 튜플
# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"안효섭", "이도현", "김민규"}
python = set(["안효섭", "송강"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("옹성우")
print(python)

# java를 잊었어요
java.remove("김민규")
print(java)


# type_change
# 자료구조의 변경
# 커피숍
menu = {"스무디", "라떼", "에이드"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))



