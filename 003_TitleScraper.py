# Title Scraper

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try: 
		bs = BeautifulSoup(html.read(), 'html.parser')
		#title = bs.title
		title = bs.body.h1
	except AttributeError as e:
		return None

	print( html.info() )
	print( html.geturl() )
	return title

#title = getTitle('http://www.data-blaze.de')
#title = getTitle('http://www.spiegel.de')
#title = getTitle('https://github.com/Ket0')
#title = getTitle('https://github.com')

if title == None:
	print('Title could not be found. :/')
else:
	print(title)