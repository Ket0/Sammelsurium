https://www.crummy.com/software/BeautifulSoup/bs4/download/4.9/
https://www.crummy.com/software/BeautifulSoup/

soup = BeautifulSoup(html_doc, 'html.parser')

# Filterklasse

# Welche Attribute können hier verwendet werden?
# class ; href ; name ; 

# Attributlisten in Datenstruktur kapseln oder nicht?
class Attribut(object):
    def __init__(self, name):
        self.name = name

def prüfe_href(tag):
    if tag.has_attr('href') == True:
        return True

def prüfe_name(tag):
    if tag.has_attr('name') == True:
        return True

def prüfe_img(tag):
    if tag.has_attr('img') == True:
        return True

def prüfe_class(tag):
    if tag.has_attr('class') == True:
        return True

def prüfe_src(tag):
    if tag.has_attr('src') == True:
        return True

def prüfe_a(tag):
    if tag.has_attr('a') == True:
        return True

def hat_href_and_name(tag):
    if ( ((check_href(tag)) and (check_name(tag))) == True):       
        return tag
        
"""
Attribute::
'area', 'base', 'br', 'col', 'embed', 
'hr', 'img', 'input', 'keygen', 'link', 
'menuitem', 'meta', 'param', 'source', 
'track', 'wbr', 'spacer', 'frame'
"""

# Suchfunktionen
def suche_Links_auf_Ebene_1_v2():
    print("\n Funktion v2 \n ...suche_Links_auf_Ebene_1_v2...\n")
    
    # Filter alle Verweise heraus, welche die 
    # Attribute href und name besitzen
    # find.all immer ein Feld übergeben?
    for link in soup.find_all(hat_href_and_name):
        print(link.get('href'))

        # folge jedem Link

def suche_Links_auf_Ebene_1_v1():
    print("\n Funktion v1 \n ...suche_Links_auf_Ebene_1_v1...\n")
    
    #such_string_ebene_1 = "/Vrz/"
    for link in soup.find_all(["a"]):
        print(link.get('href'))
