# count = 0
# for letter in 'mississippi':
#    if letter == 's':
#        count += 1
# print(count)

# n = 5
# while n != 0:
#    print(n)
#    n = n - 2

# def uses_any(word, letters):
#    for letter in word:
#        if letter in letters:
#            return True
#    return False

def version_a(word):
    for letter in word:
        if letter in 'aeiou':
            print(letter)


    print('Done')


def version_b(word):
    
