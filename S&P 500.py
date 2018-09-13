from bs4 import BeautifulSoup
import urllib


#url of the page you want to parse
url = "https://www.bloomberg.com/quote/SPX:IND"

# query the website and return the html to the variable ‘page’
page = urllib.request.Request(url)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


sName = soup.find('h1', attrs={'class': 'episode-list'})
name = sName.text.strip()

sPrice = soup.find('div', attrs={'class': 'price'})
price = sPrice.text


print(f"The {name} is at {sPrice}")


