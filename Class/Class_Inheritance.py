# 클래스 상속
# 중복되는 기능이나 변수가 있을 수 있으므로 이럴때 상속을 사용
# 상위 개념의 클래스를 만들어서 하위 개념의 클래스를 만들때 상위 개념의 클래스의 기능을 가져올 수 있는 것

class Person:
    def __init__(self):
        self.num_arm = 2
        print('Person Init')
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    # 상속을 받을려면 상속받을 클래스를 넣어주면 됨

    def __init__(self,semester):
        super().__init__()
        # 하위 클래스는 init을 할 때 항상 super를 이용해서 __init__을 해줘야 함
        print('Student Init')
        self._semester = semester
    def studying(self):
        print('공부하기')

kim = Student()
kim.greeting()
# Student는 원래 greeting을 사용할 수 없지만 상속을 받았기 때문에 부모의 메소드를 사용가능

k1 = Student(semester=2)
print(k1.num_arm)
print((k1._semester))

# Method Overriding
# 부모클래스의 함수를 그대로 가져와서 상황에 맞게 변형을 시키는 과정

class Person:
    def __init__(self):
        self.num_arm = 2
        print('Person Init')
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    # 상속을 받을려면 상속받을 클래스를 넣어주면 됨

    # def __init__(self,semester):
    #     super().__init__()
    #     # 하위 클래스는 init을 할 때 항상 super를 이용해서 __init__을 해줘야 함
    #     print('Student Init')
    #     self._semester = semester

    def greeting(self):
        super().greeting()
        print('학생입니다. 안녕하세요')
        # 부모클래스의 함수를 변형 가능

    def studying(self):
        print('공부하기')

kim = Student()
k = kim.greeting()
# 부모클래스의 함수를 현재 클래스에 맞게 변형도 가능하고, 부모클래스의 함수를 그대로 가져와서 사용가능


# 다중 상속

class Person:
    def __init__(self):
        self.num_arm = 2
        print('Person Init')
    def greeting(self):
        print('안녕하세요')

class University:
    def credit_show(self):
        print('A')


class Student(Person, University):
    # 두개의 부모를 가지는 클래스
    # 상속을 받을려면 상속받을 클래스를 넣어주면 됨


    def greeting(self):
        super().greeting()
        print('학생입니다. 안녕하세요')
        # 부모클래스의 함수를 변형 가능

    def studying(self):
        print('공부하기')

kim = Student()
kim.greeting()
kim.credit_show()
# university에 있는 함수도 사용가능

# 추상 클래스

from abc import *
# 추상 클래스를 만드는데 도움을 주는 패키지

class StudentBase(metaclass=ABCMeta):

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

    # 함수의 틀만 만들고 자식 클래스에서 메소드 구현을 하는 것

class Student1(StudentBase):
    def study(self):
        print('공부')

    def go_to_school(self):
        print('학교가기 ')

k1 = Student1()
k1.go_to_school()
k1.study()