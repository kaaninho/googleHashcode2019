def firstfun(x):
    return x + 3

def test():
    return map(firstfun, [23, 24])

with open('test.txt', 'r') as f:
    first_line = f.readline()

    print(first_line)
