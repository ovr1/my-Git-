from timeit import Timer

a = 1; b = 's'
a,b = 1, 2

t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(t1)

t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(t2)