words = 'the cat sat on the mat'.split()
print(len(words))
print(len(set(words)))

def mystery(s):
    return len(set(s)) == len(s)

print(mystery('hello'))
print(mystery('world'))

freq = mystery({'a': 2, 'b': 3, 'c': 2})
result = sorted(freq.items(), key=lambda x: x[1])
print(result)