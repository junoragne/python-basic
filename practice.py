# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")


# print(abs(-5)) 절대값
# print(pow(4, 2)) 제곱
# print(max(5, 12)) 최댓값
# print(min(5, 12)) 최솟값
# print(round(4.94)) 반올림

# from math import *
# print(floor(4.99)) 내림
# print(ceil(3.14)) 올림
# print(sqrt(16))제곱근

from random import *

# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성

# print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) #0~10 미만의  임의의 정수 값 생성

#  print(int(random() * 10))
# from random import *
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46)) #1~45 미만의 임의의 값 생성
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45)) #1~45이하의 임의의 값 생성

#Quiz)
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고
# 파이썬은 쉬워요
# """
# print(sentence3)

# junoh = "020814-1234567"

# print("성별 : " + junoh[7])
# print("연 : " + junoh[0:2])
# print("month : " + junoh[2:4])
# print("day : " + junoh[4:6])

# print("생년월일 : " + junoh[:6])
# print("뒤 7자리" +junoh[7:])
# print("뒤 7곱자리 (뒤부터) : " + junoh[-7:])

# python = "Python is Amazing"
# print(python.lower()) #문장을 소문자로 출력
# print(python.upper()) #문장을 대문자로 출력
# print(python[0].isupper()) #0번째 변수가 대문자인지 확인하는 법
# print(len(python)) #문장 글자 수 세기
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1) # 2번째 n의 위치 구하기
# print(index)

# print(python.find("Java")) #포함되어있지 않은 변수는 -1을 반환 함
# # print(python.index("Java")) index는 에러가 뜸

# print(python.count("n")) #n의 총 등장 갯수

# from random import *
# print("a" + "b")
# print("A", "b")

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# # print("Apple은 %c로 시작해요." % "A")

# # %s 로 사용하면 정수, 문자열 상관없이 출력됨
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# #방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color="빨간"))

# #방법 4

# age = 20
# color = "빨간색"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# #
# print("백문이 불여일견\n백견이 불여일타") #탈출문자
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

#\\ : 문장 내에서 \


# #\r  커서를 맨 앞으로 이동
# print("Red Apple\rpine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")
#Quiz)
#내 풀이
# server = "http://naver.com"
# server_name = server[7:10]
# server_1 = server.split("//")[-1].split(".")[0]
# server_2 = len(server_1)
# server_3 = server_1.count("e")
# print(server_3)

# print(f"pass word : {server_name}{server_2}{server_3}!")
# print(f"{server} 의 비밀번호는 {server_name}{server_2}{server_3}! 입니다. ")
# #교재 풀이
# ur1 = "http://naver.com"
# my_str = ur1.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(ur1, password))

# 리스트 []
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["Jack", "James", "White"]
# print(subway.index("Jack"))

# joe가 다음 정류장에서 다음 칸에 탐
# subway.append("Joe") #객체 추가하기
# print(subway)

# subway.insert(1, "Jung") 
# #순서 중간에 객체 삽입하기. index 입력하고 넣을 객체 입력하면 됨
# print(subway)

# print(subway.pop())
# print(subway)


