''' 상속
    - 어떤 클래스가 다른 클래스로부터 특성과 기능을 물려 받는것
    - 코드 재 사용, 일반화
    - 정의되어 있는 데이터 공간이나 메소드 재정의 또는 확장 가능(Overloading)
'''

class Car:

    def __init__(self, name, weight, size, cylinder):
        self.name = name
        self.weight = weight
        self.size = size
        self.cylinder = cylinder
        # 정의한 인자를 self.인자를 넣어라
        # car에서 받은 인자를 self.인자 에 넣어서 해당 값을 클래스에서 사용할 수 있도록 함

    def showspec(self):
        print('이름 : {}'.format(self.name))
        print('무게 : {}t'.format(self.weight))
        print('크기 : {}m'.format(self.size))
        print('배기 : {}cc'.format(self.cylinder))


# Inheritance

class  Truck(Car):

    pass
# Truck클래스는 Car라는 클래스를 상속 받겠다.

t1 = Truck('타이탄', 2.5, 4.8, 2200)
t2 = Truck('볼보', 5, 5.5, 3300)
print(t1.showspec())
print(t2.showspec())
# 상속받은 클래스가 car클래스의 메소드를 잘 출력한다.

class Sedan(Car):

    def __init__(self, name, weight, size, cylinder, color):
        super().__init__(name, weight,size, cylinder)
        # 부모 클래스에 있는 init 기능을 가지고 오겠다 라는 뜻
        self.color = color

    def showspec(self):
        super().showspec()
        # 부모 클래스에 있는 showspec 기능을 가지고 오겠다.
        # 이러면 메소드를 따로 안지정해도 됨
        print('색상 : {}'.format(self.color))


s1 = Sedan('Benz', 1.0, 1.9, 2600, 'RED')
print(s1.showspec())

# 2차 상속

class SUV(Sedan):
    pass

sv1 = SUV("Honda", 2.0, 2.1, 2400, 'BLUE')
print(sv1.showspec())

# 파이썬 내장클래스 상속

class MyDict(dict):

    def keys(self):
        k = super().keys()
        # dictionary의 keys의 기능을 상속받겠다.
        return sorted(k)

    def items(self):
        k = super().items()
        return sorted(k, key = lambda x : x[1])
        # dictionary에서 item은 두번째에 있으니깐 x[1]로 지정하고 sort

data = MyDict({'japan' : 26,
              'china' :  3 ,
              'USA' : 3,
               'KOREA' : 7})
print(data.keys())
print(data.items())
for k, v in data.items():
    print(k,v)

''' 연산자 중복
    - 언어에서 미리 정의되어 있는 일부 연산자나 메소드들에 대해 개발자 의도를 담아 처리할 수 있도록 
      클래스에서 재정의를 허용하는 것
    - class 작성을 통해 재저으이한다. 
    - 이름 앞뒤에 __가 붙어있다. 
'''

class MyStr(object):

    def __init__(self, string):
        self.string = string

    def __add__(self, string2):
        return self.string + str(string2)

a = MyStr('korea')
b = a.__add__(5)
print('\n',b)

class MyList(object):

    def __init__(self, list):
        self.mylist = list

    def __add__(self,list1):
        new_list = [x + y for x, y in zip(self.mylist, list1.mylist)] # ?

        return new_list
a = MyList([3, 6, 8, 12, 15])
b = MyList([100, 200, 300, 400, 500])
c = a + b
print(c)





