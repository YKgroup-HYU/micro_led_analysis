

# 1.6.4
number = input()
last_character = number[-1]
last_number = int(last_character)
if last_number == 0\
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:
    print("짝수입니다.")

# 예제
number = input("정수 입력 :678")
number = int(number)
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
#######################################
if number % 2 == 1:
    print("홀수입니다.")
