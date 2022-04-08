# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["안효섭", "이도현", "옹성우"]
print(subway)

# 이도현이 몇 번째 칸에 타고 있는가
print(subway.index("이도현")) # 1 > 0, 1, 2 순서이기 때문에 이도현은 1번째 칸에 탑승

# 심자윤이 다음 정류장에서 다음 칸에 탐
subway.append("심자윤")
print(subway)

# 김태연을 안효섭과 이도현 사이에 태움
subway.insert(1,"김태연") # 김태연을 1번째 칸에 태움
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

# 같은 이름의 사람이 몇 명 있는 지 확인
subway.append("안효섭")
print(subway)
print(subway.count("안효섭"))

# 정렬도 가능
num_list = [5,2,4,1,3]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,1,3]
mix_list = ["안효섭",20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list) # num_list에 mix_list를 합쳐서 확
print(num_list)