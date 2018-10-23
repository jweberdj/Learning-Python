import requests
import json

api_key = '58F1F6E8-5DE9-874A-9038-362936F352FC2E70A43E-2E28-4214-85D7-1F09B477F9A4'
payload = {'access_token': api_key}
bank_items = requests.get('https://api.guildwars2.com/v2/account/bank', params=payload).json()

item_ids = []
for item in bank_items:
    item_ids.append(str(item['id']))

print(item_ids)

payload = {'ids':''.join(str(item_ids))}
items = []
for id in item_ids:
    items.append(requests.get('https://api.guildwars2.com/v2/items/' + id).json())

for item in items:
    print(json.dumps(item['name'], sort_keys=True, indent=4))
# print(json.dumps(items[0], sort_keys=True, indent=4))
# print(json.dumps(items[4], sort_keys=True, indent=4))

#print(json.dumps(items, sort_keys=True, indent=4))


#print(json.dumps(r.json(), sort_keys = True, indent=4))