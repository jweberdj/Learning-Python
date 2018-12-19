import requests
import json

api_key = 'x'
payload = {'access_token': api_key}
bank_items = requests.get('https://api.guildwars2.com/v2/account/bank', params=payload).json()
print(requests.get('https://api.guildwars2.com/v2/account/bank', params=payload).headers)

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
