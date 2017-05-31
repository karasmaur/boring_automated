import requests, bs4, sys, os

repo = 'c:/images'

if not os.path.exists(repo):
    os.makedirs(repo)

search_word = 'Accenture'   #.join(sys.argv[1:])
url = 'https://www.google.com.br/search?q=' + search_word + '&source=lnms&tbm=isch'
google = 'https://www.google.com.br'

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

all_images = []

for a in soup.find_all(id="cnt"):
    all_images.append(a)

if all_images == []:
    print('Image link not found!')
else:
    download_image = min(4, len(all_images))

    for image in download_image:
        actual_image_link = google + download_image[image].get('href')

        res = requests.get(actual_image_link)
        res.raise_for_status()

        image_file = open(repo+'/pic.png', 'wb')

        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        print('Done! Images saved in ' + repo)









