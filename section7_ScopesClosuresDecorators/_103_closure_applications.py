
print('\n*** Method 1: Using a class ***')
class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        print(total/count)
        return total/count

a = Averager()
a.add(10)
a.add(20)
a.add(30)
a.add(40)

b = Averager()
b.add(10)
b.add(-10)
b.add(30)



print('\n*** Method 2: Using a closure instead ***')
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        print(total/count)
        return total/count
    return add

a = averager()
a(10)
a(-10)
a(30)
print(a.__closure__)

print('\tCreate a separate new closure')
b = averager()
b(10)
b(20)
b(30)
print(b.__closure__)




print('\n*** Method 2: Using a closure, with 2 free variables ***')
def averager():
    numbers = []
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        print(total/count)
        return total/count
    return add

a = averager()
a(10)
a(-10)
a(30)
print(a.__closure__)




print('\n*** Method 1: Using a class, in a cleaner way ***')
class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        print(self.total/self.count)
        return self.total/self.count

a = Averager()
a.add(10)
a.add(20)
a.add(30)
a.add(40)


print('\n*** Can be easier to write using a closure ***')
from time import perf_counter
class Timer:
    def __init__(self):
        self.start = perf_counter()

    def poll(self):
        print(perf_counter() - self.start)
        return perf_counter() - self.start

    # Make the instance callable
    def __call__(self, *args, **kwargs):
        return perf_counter() - self.start

t1 = Timer
t1()

print('\n*** Using a closure instead ***')
def timer():
    start = perf_counter()
    def poll():
        print(perf_counter() - start)
        return perf_counter() - start
    return poll

t2 = timer()
t2()


















