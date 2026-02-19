# for i in range(5):
#    print(i)


# i = 0
# while i < 5:
#    print(i)
#    i += 1

# response = ""
# while response != "quit":
#    response = input("Enter command: ")
#    print(f"You said: {response}")


# break - exit the loop immediately
# words = ["hello", "world", "target", "python"]
# for w in words:
#    print('checking:', w)
#    if w == "target":
#        print("Found it!")
#        break

# words = ["hello", "world", "target", "python"]
# for w in words:
#    print('checking:', w)
#    if w == "target":
#        print("Found it!\n")
#        continue
#    print("Not the target\n")

# continue - skip to the next iteration
# for num in range(9):
#    if num % 4 == 0:
#        continue
#    print(num) # prints odd numbers only

def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        return num
    
    
print(f(10))
