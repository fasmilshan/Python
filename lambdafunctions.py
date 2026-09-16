
from functools import reduce

def sqr(a):
    print(f'Square Of {a} is "{a*a}" ')
sqr(5)





sq=lambda a:print(f'Square Of {a} is "{a*a}" ')
sq(7)


numbers=[1,2,3,4,5,6,7,8,9,10]
print(sum(numbers))
doubled=list(map(lambda i:i*2 ,numbers))
print(doubled)


even=list(filter(lambda i:i%2==0,numbers))
print(even)


Sum=reduce(lambda a,b:a+b,numbers)
print(Sum)




