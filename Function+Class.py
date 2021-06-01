# lambda(익명함수)
# 이름없이 인수와 수식을 통해 값을 반환하는 한 줄 함수

k = lambda x, y : x * y
# 인수 : 반환할 식
print(k(10, 5))
# x와 y에 10과 5를 반환하면 x*y를 return하라

p = lambda x, y : (x+y, x-y, x*y)
print(p(6,4))
# 반환할 식을 여러개 넣을 수 있음
# Tuple로 묶어서 값을 return

mul = lambda x, y, z : x*y*z
print(mul(5,7,9))

m = ['python', lambda x: x*x, 100]
print(m[0])
print(m[1])
print(m[2])
print(m[1](5))
# 이렇게 람다함수를 리스트에 넣을 수 있고 직접 값을 넣어서 리턴 가능


'''재귀호출 함수
자기자신을 호출하는 함수
팩토리얼, 피보나치 수열 등
'''


# 팩토리얼
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

while True:
    n = input('팩토리얼 구할 숫자는? \n')
    if n.isnumeric():
        res = factorial(int(n))
        print(res)
    else:
        print('종료')
        break

# 피보나치 수열
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

f = []
while True:
    k = input('\n 몇 단계 까지??')
    if k.isnumeric():
        f.clear()
        k = int(k)
        for i in range(1, k+1):
            f.append(fibonacci(i))
        for i in f:
            print(i, end = ' ')
    else:
        print('종료')
        break


'''고차함수
인자로 다른 함수를 전달받거나 함수를 반환하는 함수
ex) filter(함수, 리스트) 내장함수
리스트에 있는 값을 하나씩 함수에 전달해서 True인 결과만 모아서 리스트 형태로 반환
'''


def func(x):

    if x % 2 == 0:
        return True

if __name__ == '__main__':
    a = [1,2,3,4, 10, 8, 20, 22, 23, 25, 30]
    ls = list(filter(func, a))
    print(ls)

lst = list(filter(lambda a : a%2 == 0, a))
print(lst)

'''map(함수, 시퀀스) 내장함수
시퀀스 : 리스트 데이터형태
'''
def func(x):
    return x * x

lst = list(map(func, a))
print(lst)

print(list(map(lambda x : x*x, a)))

def cube(x):
    return x * x * x
def quad(x):
    return x * x * x * x

def agency(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))

    return result

print(agency(cube, [3,2,6]))
print(agency(quad, [3,2,6]))

''' 클래스
def 함수명(self, 인자 ..)
self 키워드 : 클래스 정의 시 모든 함수의 첫번째 인자는 반드시 self이다.
    객체 자신의 참조를 의미
    self를 통해 클래스 내의 변수, 함수에 접근 가능
생성자 : 객체가 생성될 때 저절로 수행되는 메소드
    __init__이름으로 정의
'''

class Hello:
    def __init__(self):
        self.count = 0

    def sayhello(self, hellostring, count = 1):
        for i in range(count):
            print(hellostring)
        self.count += count

    def showcount(self):
        return self.count

h1 = Hello()
print(h1.sayhello('Hi', 4))
m = Hello()
print(m.sayhello('Bye', 2))

print(h1.showcount())
print(m.showcount())
print(h1.count)
# 외부에서 클래스 안의 변수가 출력되기 때문에 은닉해야함
# count를 __count로 변경하면 됨


''' 접근 지정 
Public : 허용 
Private : 허용 X

은닉을 원할때 : __name, _name
'''



