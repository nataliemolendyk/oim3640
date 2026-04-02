# try:
#    x = int('hello')
#    print('success')
# except ValueError:
#    print('oops')
# print('done')

# try:
#     x = int('42')
#     print('success')
# except ValueError:
#    print('oops')
# print('done')

import requests
data = requests.get('https://oim.108122.xyz/mass').json()
print(type(data))
print(type(data['data']))
print(type(data['data'][0]))