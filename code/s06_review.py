# for i in range(4):
#   print("Iteration:", i)
#   print("Square:", i * i)
#       print()

# x = "42"
# type(x)
# print(type(x))

# y = 42
# type(y)
# print(type(y))

# z = 42
# type(z)
# print(type(z))

# name = "Python"
# print(name * 3)
# print(name + "3")

# def double(x):
#   return x * 2
# print(double(5))
# print(double("Hi"))

# a = 5    # integer is immutable type
# b = a
# a = 10
# print(b)
# print(a)

# x = 10
# def f():
#   message = "Hello"
#     x = 5
#     return x

# print(f())
# print(x)
# print(message)

# Draw a square
# """
# 🥩🥩🥩🥩
# 🥩🥩🥩🥩
# 🥩🥩🥩🥩
# 🥩🥩🥩🥩
# """

# def draw_square(size):
#     for i in range(size):
#        print("🥩" * size)
#       for j in range(size):
#          print("🥩", end="")
#        print()



"""
Create a function to draw a triangle
🥩          1 = 0 + 1
🥩🥩        2 = 1 + 1
🥩🥩🥩      3 = 2 + 1
🥩🥩🥩🥩    4 = 3 + 1

In row i, how many steaks are there?
"""
def draw_triangle(rows):
    for i in range(rows):
        print("🥩" * (i + 1))

def draw_traingle(size):
        for i in range(1, size + 1):
            print("🥩" * i)

draw_triangle(4)

"""
Draw a triangle like this (size = 5)

    #     4 + 1 = 5  5 - 0 - 1 = 4
   ##     3 + 2 = 5  5 - 1 - 1 = 3
  ###     2 + 3 = 5  5 - 2 - 1 = 2
 ####     1 + 4 = 5  5 - 3 - 1 = 1
#####     0 + 5 = 5

for i in range(sizes):
In row i, how many spaces are there? size - i - 1 how many #s are there? i + 1
"""
