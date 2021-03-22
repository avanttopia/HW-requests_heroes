import requests
heroes_list = ['Hulk', 'Captain America', 'Thanos']


def get_max_intelligence(heroes_list):
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    max_intelligence = 0
    hero = ''
    for i in heroes_list:
        url_hero = url + i
        resp = requests.get(url_hero)
        heroes_list = resp.json()['results']
        if int(heroes_list[0]['powerstats']['intelligence']) > max_intelligence:
            max_intelligence = int(heroes_list[0]['powerstats']['intelligence'])
            hero = i
    return hero


print(get_max_intelligence(heroes_list))
