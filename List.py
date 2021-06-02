''' 집단 자료형
    - list : []
    - Tuple : ()
    - dict : {key : value}
    - set : {}
'''
''' List
    - 하나의 변수명으로 여러 객체를 기억할 수 있는 집단형 자료 
    - 요소들을 순서대로 저장하는 시퀀스 자료 (인덱싱, 슬라이싱 등 가능)
    - 요소의 크기, 요소의 유형, 데이터 크기 등 구애됨이 없는 동적 구조 
    - 요소를 변경 가능 
'''

my_list = ['한국', '미국', '중국', '일본']

print(my_list[0])
print(my_list[-4])
print(len(my_list))
print(my_list[:2])
my_list[2] = 2500
print(my_list)
my_list[3] = '대만'
print(my_list)

# 변경가능

# list에 연산자 사용 가능
a = list(range(5))
print(a)
print(a+a)
print(a*3)

# 중첩 리스트
a = [1, 2, 3]
b = [a, '한국', '미국']
print(b)
print(b[0][2])
print(b[1])

a = [1, 7, 2, 6, 7, 8]
a.append(0)
# 맨끝에 0을 추가
print(a)
a.insert(2, '김')
# 인덱스 2번에 김을 추가

print(a.count(7))
# 7의 개수

print(a.index('김'))

a.remove('김')
print(a)

a.extend([40,50,60])
# 리스트를 추가
print(a)

a.append([40,50,60])
print(a)
# 리스트안에 또 다른 리스트 추가

a = ''' 김영민, 69, 100, 100
박동식, 100, 98, 98
최민규, 88, 75, 43
김철규, 88, 76, 54
신형균, 99, 77, 12'''
print(a)
b = a.split('\n')
print(b)
# 리스트로 변환됨

for i in range(len(b)):
    b[i] = b[i].split(',')
    # ,를 기준으로 split

print(len(b))
print(len(b[0]))

for i in range(len(b)):
    sum = 0
    for j in range(1,4):
        b[i][j] = int(b[i][j])
        sum += b[i][j]
    b[i].append(sum)
    av = int(sum/3)
    b[i].append(av)
print(b)

# 집단형 데이터 사용
data= [ '김동일', '이성호', '강운규', '임동현']
for i in data:
    print(i, end = ' \n')

# range()와 len()사용
for i in range(len(data)):
    print(i, ' ', data[i], end = ' \n')

# enumerate() 사용
for i, dt in enumerate(data):
    print(i, ' ', dt, end = ' \n')



