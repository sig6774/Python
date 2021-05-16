class Flight:
    nation = 'Korea' # 클래스 변수
    # 생성자와 초기화
    def __init__(self, number, length = 30):
        # Flight라는 객체를 생성할때 number도 초기화
        # length는 디폴트값으로 지정 가능
        self._number = number
        self._length = length
        # print('Flight init')
        # super().__init__()
        # # Flight의 부모클래스를 시작하는 것 즉, 상속

        self.__passenger_num = 0
        # __는 외부에서는 passenger_num이라는 변수에 접근 불가

    # 메소드 : 클래스 안의 함수
    def number(self):
        return self._number

    def length(self):
        return  self._length

    def add_passenger(self, num):
        self.__passenger_num += num
        print(self.__passenger_num)
f = Flight(number = 'KE081')
f1 = Flight(number= 'KE032', length=50)
# 객체 생성
# 이때 init이 수행됨
# length에 값을 할당하지 않아도 디폴트값이 출력되며 값을 넣어주면 변경 가능

# print(f.number())
# print(f.length())
# print(f1.length())

# f.add_passenger(10)

print(Flight.nation)
# 클래스 변수는 객체를 생성하지 않아도 클래스명 자체에서도 접근 가능

