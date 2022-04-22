

import requests

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
nitrogen = (data['list'][0]['components']['co'])
nitrogen_dioxide = (data['list'][0]['components']['co'])
ozone = (data['list'][0]['components']['co'])
sulfur_oxide = (data['list'][0]['components']['co'])
partical_matter = (data['list'][0]['components']['co'])
partical_matter2 = (data['list'][0]['components']['co'])
nh3 = (data['list'][0]['components']['co'])
