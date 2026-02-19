# score = int(input("Enter your score: "))
            
# if score >= 60:
#    print("Pass")
# elif score >= 90:
#    print("A")
# else:
#    print("Fail")

# def mystery(x):
#    if x > 0:
#       return "positive"
#    print("done")

# result = mystery(5)
# print(result)

def check(n):
    if n % 2 ==0:
        if n % 3 == 0:
            print("A")
        else:
            print("B")
    else:    
            print("C")

check(6)
check(8)
