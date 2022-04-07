print("Hello World")

'''숫자형 자료형'''
a = 1
b = 2
print(a+b)
print(-10)
print(3.14)
print(1000)
print(3+5)
print(3*2)
print(10/5)

'''문자열 자료형'''
print('풍선')
print("동방신기")
print("ㅋ"*9)

''' 참 / 거짓 '''
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

''' 변수 '''
animal = "강아지"
name = "쪼리"
age = 4
hobby = "산책"
is_adult = age >= 3
kind = "골든리트리버"

print("우리집 " + animal + " 이름은 "  + name + "이다")
print(name+"는 " + str(age) +"살이며, " +hobby+"를 좋아한다")
print(name+"은 어른일까요? " +str(is_adult))
print(name,"의 종류는", kind , "입니다")
# 숫자형이나 불린형을 문자형으로 출력할 땐 앞에 str()을 붙여서 써줘야한다.


''' 복습 '''
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : XX행 열차가 들어오고 있습니다.

station1 = "문산"
station2 = "신도림"
station3 = "인천공항"
print(station1+"행 열차가 들어오고 있습니다")
print(station2+"행 열차가 들어오고 있습니다")
print(station3+"행 열차가 들어오고 있습니다")