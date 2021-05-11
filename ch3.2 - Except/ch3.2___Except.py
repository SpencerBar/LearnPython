def func(divideBy):
 try:
    return 42 / divideBy
 except ZeroDivisionError:
    print('Error: Invalid argument.')
print(func(2))
print(func(12))
print(func(0))
print(func(1))
