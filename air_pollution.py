

import requests


def get_air_index_value(air_index):
    value = None
    if air_index == 1:
        value = 'Good'
    if air_index == 2:
        value = 'Fair'
    if air_index == 3:
        value = 'Moderate'
    if air_index == 4:
        value = 'Poor'
    if air_index == 5:
        value = 'Very Poor'
    return value


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Cache-Control': 'max-age=0',
}

params = {
    'lat': '21.437273',
    'lon': '40.512714',
    'appid': '9df3f65223f5d0da919ec90525134833',
}

response = requests.get('https://api.openweathermap.org/data/2.5/air_pollution', headers=headers, params=params)

data = response.json()

carbon = (data['list'][0]['components']['co'])
nitrogen = (data['list'][0]['components']['no'])
nitrogen_dioxide = (data['list'][0]['components']['no2'])
ozone = (data['list'][0]['components']['o3'])
sulfur_oxide = (data['list'][0]['components']['so2'])
partical_matter = (data['list'][0]['components']['pm2_5'])
partical_matter2 = (data['list'][0]['components']['pm10'])
nh3 = (data['list'][0]['components']['nh3'])

print("Air status is {}".format(get_air_index_value(data['list'][0]['main']['aqi'])))
print(f'Carbon in air is {carbon}')
print(f'nitrogen in air is {nitrogen}')
print(f'nitrogen_dioxide in air is {nitrogen_dioxide}')
print(f'ozone in air is {ozone}')
print(f'sulfur oxide in air is {sulfur_oxide}')
print(f'Partical matter in air is {partical_matter}')
print(f'partical_matter 10 in air is {partical_matter2}')
print(f'nh3 in air is {nh3}')

