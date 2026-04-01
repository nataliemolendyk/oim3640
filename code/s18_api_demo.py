import requests

# response = requests.get('https://oim.108122.xyz/words/random')
# print(response.json())   # a random word!

response = requests.get(
    'https://oim.108122.xyz/words/random',
    headers={'X-Token': 'natalienatalie'},  # your first name x2
)
# print(response.json())
data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

for town in data['data'][:351]:
    print(f"{town['name']}: pop {town['population']:,}")
