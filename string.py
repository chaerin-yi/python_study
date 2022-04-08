''' 문자열 '''
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)


''' 슬라이싱 '''

jumin = '040115-1234567'

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])  

print("생년월일 : " +jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " +jumin[7:]) # 7부터 끝까지
print("뒤에서부터 7자리 : " +jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지


''' 문자열 처리함수 '''
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "JAVA")) #Python이라는 단어를 JAVA로 바꿈

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 5번째 n 다음에 나오는 n은 몇번째 자리인지 
print(index)

print(python.find("Java"))
# print(python.index("Java")) # error
print("hi")
print(python.count("n"))

''' 문자열 포맷 '''
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s를 좋아해요 " % "파이썬")
print("Apple은 %c로 시작해요." %"A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "노란"))

#방법 2
print("나는{}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

#방법 3
age = 20
color = "하늘"
print(f"나는 {age}살이며, {color}색을 좋아해요")


''' 탈출문자 '''
#\n 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

#\" \' : 문장 내에서 따옴표 역할
# 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다")
print("저는 \'나도코딩\'입니다")

# \\ : 문장 내에서 \
print("C:/Users/MSI/Desktop/python/0321/string.py")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 ( 한 글자 삭제)
print("Red\bApple")

# \t : 탭
print("Red\tApple ")


''' 복습 '''
# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
# http:///naver.com
# 조건 1 : http:// 부분은 제외 => naver.com
# 조건 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 조건 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# ex) 생성된 비밀번호 : nav51!

#url = "http://naver.com"
url = "http://daum.net"
my_str = url.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str -> 0~5 직전까지 (0,1,2,3,4) 규칙 2
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0} 의 비밀번호는 {1}입니다" .format(url, password))






