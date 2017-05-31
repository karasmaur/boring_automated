import requests, bs4, webbrowser, os

url = 'https://xkcd.com/'

if not os.path.exists('c:/xkcd'):
    os.makedirs('c:/xkcd')

while not url.endswith('#'):
    print('Downloading comic thingy from '+url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic IMAGE.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image '+comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('c:/xkcd/', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')

print('Done.')