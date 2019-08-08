# Создать класс структуры данных Стек, Очередь.
# Создать класс комплексного числа и реализовать для него арифметические операции.


class Stack:

    def __init__(self):
        self._stack = []

    def pop(self):
        if len(self._stack) < 1:
            return None
        return self._stack.pop()

    def push(self, value):
        self._stack.append(value)

    def show(self):
        return self._stack


class Queue:

    def __init__(self):
        self._queue = []

    def _size(self):
        return len(self._queue)

    def pop(self):
        if self._size() < 1:
            return None
        return self._queue.pop(0)

    def push(self, value):
        self._queue.append(value)

    def show(self):
        return self._queue


class Complex:
    def __init__(self, real, imagine):
        self._real = real
        self._imagine = imagine

    def __add__(self, other):
        return Complex(float(self._real + other._real), float(self._imagine + other._imagine))

    def __sub__(self, other):
        return Complex(float(self._real - other._real), float(self._imagine - other._imagine))

    def __mul__(self, other):
        return Complex(float(self._real * other._real - self._imagine * other._imagine), float(self._imagine * other._real + self._real * other._imagine))

    def __str__(self):
        return '%.2f+%.2fj' % (self._real, self._imagine)


stack = Stack()
print(stack.show())
stack.push('1')
stack.push('2')
stack.push('3')
print(stack.show())
print(stack.pop())
print(stack.pop())
print(stack.show())

print('='*5)

queue = Queue()
print(queue.show())
queue.push('1')
queue.push('2')
print(queue.show())
print(queue.pop())
print(queue.pop())
print(queue.show())

print('='*5)

num1 = Complex(float(2), float(1))
num2 = Complex(float(3), float(4))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
