import requests, sys, webbrowser, bs4

search_term = ''.join(sys.argv[1:])
link = 'https://www.google.com.br/search?q='+search_term

print('Googling...')

res = requests.get(link)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

top_search = soup.select('.r a')

open_result = min(5, len(top_search))

for i in range(open_result):
    webbrowser.open('https://www.google.com.br/' + top_search[i].get('href'))