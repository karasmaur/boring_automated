import requests, bs4

res = requests.get('http://tempo.clic.com.br/rs/porto-alegre')
res.raise_for_status()
weather = bs4.BeautifulSoup(res.text, 'lxml')

elem = weather.select('.mainItem span')[0]
print elem.getText().strip()