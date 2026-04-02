import requests
from dotenv import load_dotenv
import os


# GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#    print(msg)

# POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#              json={'message': 'Hello from Natalie!'},
#              headers={'X-Token': 'natalienatalie'})

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Don't hardcode this!
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')

print(url)

data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")
