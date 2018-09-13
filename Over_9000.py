from bs4 import BeautifulSoup
import requests
import pdb



url = "https://www.discogs.com/James-Ingram-With-Michael-McDonald-Yah-Mo-B-There/master/122453"
url2 =  "https://www.funimation.com/shows/dragon-ball-super/"
page = requests.get(url2)
print(page.cookies)
#pdb.set_trace()
soup = BeautifulSoup(page.content, 'html.parser')

name = soup.find('h1', attrs={'class': 'episode-list'})


#print(name)