# 자료구조 : 배열 기반의 연속 방식, 포인터 기반의 연결 방식
# 연속 : 데이터를 연속한 주소에 저장, array나 list
# 포인터 : Linked List, 포인터를 가져서 아이템이 링크로 연결
# 연속은 중간에 삭제과정이 일어나면 뒷부분을 전부 바꿔야함, 검색에 있어서는 더 빠름
# 연결방식은 삭제과정이 일어나도 뒷부분을 바꾸지 않아도 됨, 검색은 연속보다 느림

# Stack
# 배열의 끝에서만 데이터를 접근할 수 있는 선형 자료구조 (후입선출)
# Push : 스택 맨끝에 값을 삽입
# Pop : 맨끝의 값을 반환하는 동시에 제거
# Top/Peek : 맨끝의 항목을 조회


# 배열 기반의 스택
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    # 비어있는지 확인

    def push(self, value):
        self.items.append(value)
    # 값 추가

    def size(self):
        return len(self.items)
    # 스택의 길이 출력

    def __repr__(self):
        return '{}'.format(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
            # 후입선출이니깐 끝에서 부터 출력
        else:
            print('Empty')
    # 맨끝의 항목 조회

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            return "Stack is Empty"
    # 항목 조회


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push(5)
    stack.push(10)
    print(stack)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())




# 포인터 기반 스택
class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer
        # 값과 포인터를 초기화

class Stack1(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        # 헤드에 노드를 만들어줌
        # 노드는 헤드와 값으로 구성되어 있음
        # 데이터가 들어올때마다 head가 업데이트

    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.pointer
            # node가 None일때 까지 반복

        return count

    def pop(self):
        if self.head:
            node = self.head
            self.head = node.pointer
            return node.value
        else:
            print('Empty')

    def peek(self):
        if self.head:
            return self.head.value
        else:
            print('Empty')

    def __repr__(self):
        item = []
        node = self.head
        while node:
            item.append(node.value)
            node = node.pointer
        item.reverse()
        # Stack이 거꾸로 되어 있기 때문에
        # [1 2 3] -> [3 2 1]
        return '{}'.format(item)

if __name__ == '__main__':
    stack = Stack1()
    print(stack.isEmpty())
    stack.push(5)
    stack.push(10)
    print(stack)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    # 후입선출이기 때문에 10이 도출

# QUE
# 큐는 스택과 다르게 항목이 들어온 순서대로 접근 가능
# 선입 선출 (First In, First Out)
# enqueue : 큐를 뒤쪽에 항목 삽입
# dequeue : 큐를 앞쪽 항목을 반환
# peek/front : 큐 앞쪽의 항목 조회


# 배열기반 큐
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, value):
        self.items.insert(0, value)
        # 데이터를 앞에 넣어줘야하기 때문에 insert를 사용해서 인덱스 지정

    def size(self):
        return len(self.items)

    def __repr__(self):
        return '{}'.format(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        # 맨뒤에 있는 인덱스를 가져오기 위해 사용
        # 선입 선출이기 때문에 [2 1 3 4] peek -> 4
        else:
            print('Empty')

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            return 'Empty'


if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(10)
    # 가장 먼저 들어온 3이 가장 뒤에 있다
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    # 가장 먼저 들어온 3이 출력되는 것을 알 수 있다.


# 두개의 스택을 이용한 큐
class Queue1(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
            # in_stack에 있는 걸 뽑아서 out_stack으로 옮김
            # out_stack에는 in_stack과 저장 순서가 반대가 되기 때문에
            # 이러한 과정을 거치면 que와 작동 구조가 같아짐

    def enqueue(self, item):
        return self.in_stack.append(item)

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
            # out_stack이 비어있으면 transfer해라

        if self.out_stack:
            return self.out_stack[-1]
        # 큐는 선입선출이기 때문에 out_stack의 맨 끝의 값을 출력하면 큐의 작동원리와 같아짐
        else:
            return 'Empty'

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return '{}'.format(self.out_stack)
        # 큐와 같이 출력
        else:
            return 'Empty'

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            return 'Empty'

if __name__ == '__main__':
    queue = Queue1()
    print(queue.isEmpty())
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(10)
    # 가장 먼저 들어온 3이 가장 뒤에 있다
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    # 가장 먼저 들어온 3이 출력되는 것을 알 수 있다.
    # 두개의 스택으로 큐를 구현할 수 있다.

# 포인터기반 큐
class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer


class Queue2(object):
    def __init__(self):
        self.head = None
        self.tail = None
        # 포인터가 두개 필요

    def isEmpty(self):
        return not bool(self.head)

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            # 새로만든 데이터에 head를 연결해줌
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node

    # enqueue 잘모르겠음

    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.pointer

        return count

    def peek(self):
        return self.head.value

    def __repr__(self):
        items = []
        node = self.head
        while node:
            items.append(node.value)
            node = node.pointer
            # 다음 포인터를 가르키게 함

        items.reverse()
        return '{}'.format(items)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            # 다음 노드로 연결
            return value
        else:
            print('Empty')

if __name__ == '__main__':
    queue = Queue2()
    print(queue.isEmpty())
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(10)
    # 가장 먼저 들어온 3이 가장 뒤에 있다
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())


# 스택을 활용하여 문자열 반전
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    # 비어있는지 확인

    def push(self, value):
        self.items.append(value)
    # 값 추가

    def size(self):
        return len(self.items)
    # 스택의 길이 출력

    def __repr__(self):
        return '{}'.format(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
            # 후입선출이니깐 끝에서 부터 출력
        else:
            print('Empty')
    # 맨끝의 항목 조회

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            return "Stack is Empty"
    # 항목 조회


def reverse_with_stack(input):
    s = Stack()
    s1 = len(input)
    for i in range(0, s1):
        s.push(input[i])
    a = []
    for i in range(0, s1):
        a.append(s.pop())
    return a

print(reverse_with_stack('donga'))


