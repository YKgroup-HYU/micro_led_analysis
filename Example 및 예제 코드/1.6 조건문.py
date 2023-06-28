# 1.6.1
number = 100
number += 10
number += 20
number += 30
print("number:",number)

# 1.6.2
print(10 == 100)
print(10 != 100)
print(10 < 100)
print(not True)
print(True and False)
print(True or False)

# 1.6.3
a = 1234
b = 13456
if a > b:
    print('a')
else:
    print('b')

number = input("정수 입력: ")
number = int(number)
if number > 0:
    print("양수입니다.")
if number < 0:
    print("음수입니다.")
if number == 0:
    print("0입니다.")

# 1.6.4
number = input("정수 입력 :")
last_character = number[-1]
last_number = int(last_character)
if last_number == 0\
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:
    print("짝수입니다.")

# 예제
number = input("정수 입력 :")
number = int(number)
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
#######################################
if number % 2 == 1:
    print("홀수입니다.")
