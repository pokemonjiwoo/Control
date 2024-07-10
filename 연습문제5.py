#1. 사용자로부터 입력받아
text = input("조회할 요소를 입력하세요.")
#2. fruit 변수는 리스트
fruit = {"봄" : "딸기", "여름" :"토마토" , "가을" : "사과"}
#3. 입력받은 값이 fruit 요소로 있는지 확인
if text in fruit. values():
    print("정답입니다.")
else :
    print("오답입니다.")