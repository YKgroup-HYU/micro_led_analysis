# 1.4.1 (터미널에서 변수 하나씩 입력하여 실행)
myInt = 4
myReal = 2.5
myChar = 'a'
myString = 'hello'

# 1.4.2
myInt = 4
myString = 'hello'
print(myInt)
print(myString)

print("hello""everybody""!")
print("hello"+"everybody"+"!")
print("hello","everybody","!")

print(1+2+3)
print(1,2,3)

# 1.4.3
a = 2
b = 3
print('구구단 {0} X {1} = {2}'.format(a,b,a*b))

# 1.4.4
number = input("숫자를 입력하세요: ")
print(number)

# 1.4.5
a = input()
print('첫번째로 입력 하신 것은 : {} 입니다.'.format(a))
b = input()
print('두번째로 입력 하신 것은 : {} 입니다.'.format(b))

# 1.4.6
myInt = 4
myReal = 2.5
myChar = 'a'
myString = 'hello'
a = [1,2,3]
print(type(4))
print(type(2.5))
print(type(myChar))
print(type(a))

# 1.4.7
a = int(3.141592)
b = int('10')
c = float(10)
d = float('10')

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

# 1.4.8
a=str(10)
b=str(3.141592)
print(a,type(a))
print(b,type(b))

# 예제
str_input = input("숫자입력: ")
num_input = float(str_input)
print(num_input,"inch")
print((num_input*2.54),"cm")
