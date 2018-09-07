import requests
import re
from bs4 import BeautifulSoup

# pattern = re.compile(r'\d+')
#
# req = requests.get("http://fucai.eastday.com/LotteryNew/K3Result.aspx")
#
# soup = BeautifulSoup(req.text,"html.parser")
#
# num = soup.find_all('span')[:3]
#
# list = pattern.findall(num.__str__())
#
# print(list[0]+','+list[1]+','+list[2])


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(3))

l = ["a","b","c","d"]

print(l[0:3])

gen = (x * x for x in range(10))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

def odd():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

print(odd().__next__())
print(odd().__next__())
print(odd().__next__())
print(odd().__next__())

sean = abs

print(sean(-10))

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, -6, abs))

l = [1,2,3,4,5]

def f(x):
    return x-1;

r = map(f,l)
print(list(r))


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def build(x, y):
    return lambda: x * x + y * y

f = build(1,2)

print(f())
print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print("007")

print(now())