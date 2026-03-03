# def has_vowel(s):
#    i = 0
#    while i < len(s):
#        if s[i] in 'aeiou':
#            i += 1
#            return True
#    return False

# def has_digit(s):
#    for c in s:
#        if c.isdigit():
#            return True
#        else:
#            return False

# print(has_digit('iPhone15'))
# print(has_digit('4ever'))
# print(has_digit('hello'))

# def has_lower(s):
#    for c in s:
#        if 'c'.islower():
#            return True
#        else:
#            return False
        
# print(has_lower('NASA'))
# print(has_lower('Python'))
# print(has_lower('copilot'))

# def check_vowel(s):
#    for c in s:
#        result = (c in 'aeiou')
#    return result

# print(check_vowel('orange'))
# print(check_vowel('lemon'))
# print(check_vowel('kiwi'))

# def any_vowel(s):
#    flag = False
#    for c in s:
#        flag = flag or (c in 'aeiou')
#    return flag

# print(any_vowel('rhythm'))
# print(any_vowel('cafe'))
# print(any_vowel('ski'))

# def all_alpha(s):
#    flag = True
#    for c in s:
#        flag = flag and c.isalpha()
#    return flag

# print(all_alpha('Babson'))  
# print(all_alpha('OIM3640'))   
# print(all_alpha('hello!'))  

# def has_space(s):
#    for c in s:
#        if c == ' ':
#            break
#            return True
#    return False

# print(has_space('ice cream'))  
# (has_space(' hello'))     
# print(has_space('pizza'))       

def all_digit(s):
    for c in s:
        if not c.isdigit():
            return False
    return True

print(all_digit('911'))      
print(all_digit('3.14'))    
print(all_digit('OIM3640'))  
