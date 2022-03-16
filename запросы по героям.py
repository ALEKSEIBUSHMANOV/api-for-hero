

import requests

namesearch_url = "https://superheroapi.com/api/2619421814940190/search/"
response = requests.get(namesearch_url)
superheroes = ['Hulk', 'Captain America', 'Thanos']
b = {}
for name in superheroes:
    response = requests.get(namesearch_url + name)
    a = int(response.json()['results'][0]['powerstats']['intelligence'])
    b[name] = a
print(sorted(b.items(), key=lambda item: (-item[1], item[0]))[0][0])


