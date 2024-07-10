#해당 수가 5와 10 사이에 있으면 ok를 입력, 그렇지 않으면 no 입력
num = int(input("임의의 숫자를 입력하세요."))

if 5 < num < 10 :
    print(" ok ")
elif num <= 5 :
    print(" no ")
elif num <= 10 :
    print(" no ")
# 다른 방법
#if 5 < num < 10 :
 #   print(" ok ")
#else :
  #  print(" no ")



# and, or 연산자
apple = '사과'
banana = '감자'

if apple == '사과' or banana == '바나나' :
    print("문자열이 모두 정확합니다.")


var = {1, 2, 3}
if 3 in var :
    print("숫자 3이 var 변수에 있습니다.")
