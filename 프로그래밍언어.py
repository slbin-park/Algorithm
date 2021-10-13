add1 = lambda x, y: x + y
add2 = lambda x: lambda y: x + y
max = lambda x: lambda y: x if (x > y) else y
add3 = lambda x: lambda y: lambda z: x + y + z
add32 = lambda x: (lambda y: (lambda z: x + y + z))

test1 = add1(10, 20)
test2 = add2(10)(20)
test3 = max(20)(10)
test4 = add3(10)(20)(30)
test5 = add32(10)(20)(30)

print(test3)
print(test4)