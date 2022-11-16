def generator2():
    yield 'a'
    yield 'b'
    yield 'c'
    yield from [11, 22, 33, 44]
    yield from (12, 23, 34)
    yield from range(3)


for i in generator2():
    print(i, end=' , ')

