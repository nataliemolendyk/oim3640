# stocks = input('Enter the stocks: ')
# stocks[0]
# print(stocks[0])
# stocks[-1]
# len(stocks)
# stocks[19]
# stocks[18]

def count_vowels(s):
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
            
    return count

print(count_vowels('apple'))
print(count_vowels('sky'))
print(count_vowels('ski'))
