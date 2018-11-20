from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getAllLinks0():
	#html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
	html = urlopen("http://www.data-blaze.de")
	bs = BeautifulSoup(html, "html.parser")

	# Entfernt das HTML Markup und 
	# schreibt nur den eigentlichen 
	# Link heraus
	for link in bs.find_all("a"):
		if "href" in link.attrs:
			print(link.attrs["href"])

def getAllLinks1():
	#html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
	html = urlopen("http://www.data-blaze.de")
	bs = BeautifulSoup(html, "html.parser")

	# Schreib den kompletten HTML Markup heraus
	seq_links = bs.find_all("a")
	print(seq_links)

# def getAllImages():
# 	html = urlopen("http://www.data-blaze.de")
# 	bs = BeautifulSoup(html, "html.parser")
	
# 	myImagesOnSite = bs.find_all("img")
# 	print(myImagesOnSite)

	#for image in bs.find_all("img"):
		#if "img" in image.attrs:
		#	print(image.attrs["img"])
	#	print(bs.find_all("img"))

def getImage():
	html = urlopen("http://www.data-blaze.de")
	bs = BeautifulSoup(html, "html.parser")
	links = bs.find('figure').find_all('img', src=True)
	for link in links:
		timestamp = time.asctime() 
		txt = open('%s.jpg' % timestamp, "wb")
		link = link["src"].split("src=")[-1]
		download_img = urllib2.urlopen(link)
		txt.write(download_img.read())
		txt.close()

# # # main # # #

print("getAllLinks0()\n")
getAllLinks0()

print("\ngetAllLinks1()\n")
getAllLinks1()

#print("\ngetAllImages()\n")
#getAllImages()
getImage()