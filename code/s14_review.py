# s = 'python'
# lst = ['python', 'javascript', 'r', 'cplusplus']
# s + 'language'
# s * 3
# lst * 3
# lst[:3]
# s[:3]
# 't' in s
# 't' in lst
# 'r' in lst
# sorted[lst]

# making an alias
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)
print(a is b)

# making a copy
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a, b)
print(a is b)
