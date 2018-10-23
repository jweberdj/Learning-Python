import reqeusts
import json

api_key = '58F1F6E8-5DE9-874A-9038-362936F352FC2E70A43E-2E28-4214-85D7-1F09B477F9A4'
payload = {}
r = requests.get('https://api.guildwars2.com/v2/achievements')
r.json()
print(r)