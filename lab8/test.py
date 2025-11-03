x = 42
y = 1
p = 3.14
s = '42'
li = ['42', (4, 5, 6, 7), None]
d = {
    p: [s, li],
    'x': y,
    y: p,
}

print(d[3.14][1][-1])

a = 1
b = 2
a = a + b
b = a * b
a -= 1

print(b - a)

def decremented(x):
    return x - 1

def foo(x):
    x += 2
    return x + decremented(x)

x = 3
x = foo(x)

print(x)

s = 'abc'
t = ''
for c in s:
    t = c + t

print(t)

t = ['a', 'b', 'c']
for i in range(len(t)):
    m = t[i]
    t[i] = t[i-1]
    t[i-1] = m

print(t)