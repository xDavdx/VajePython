from bs4 import BeautifulSoup
import codecs

# Odpre datoteke z načinom r -> read
fileing = codecs.open("following.html", 'r', 'utf-8')
fileers = codecs.open("followers.html", 'r', 'utf-8')

# Prebere obe datoteki (vse kar je v datoteki zapisanega)
followingHTML = fileing.read()
followersHTML = fileers.read()

# Inicializira razreda tipa BeautifulSoup, 1. argument je string (ki vsebuje html kodo), 2. pa pove, da je string tipa html
souping = BeautifulSoup(followingHTML, 'html.parser')
soupers = BeautifulSoup(followersHTML, 'html.parser')

# Nov seznam (array) po imenu following
following = []
# Najdi vse html objekte, ki vsebujejo class "_2g7d5 notranslate _o5iw8" in ga vsakič daj v spremenljivko one
for one in souping.find_all("a", attrs={"class": "_2g7d5 notranslate _o5iw8"}):
	# Doda v seznam (array) novega najdenega userja
    following.append(one.string)

# Nov seznam (array) po imenu followers
followers = []
# Najdi vse html objekte, ki vsebujejo class "_2g7d5 notranslate _o5iw8" in ga vsakič daj v spremenljivko one
for one in soupers.find_all("a", attrs={"class": "_2g7d5 notranslate _o5iw8"}):
	# Doda v seznam (array) novega najdenega userja
    followers.append(one.string)

# Naloga: 
# Zgradi tri sezname: 
#    1. seznam naj vsebuje: userje, ki jim slediš in oni tudi tebi
#    2. seznam naj vsebuje: userje, ki jim slediš in oni tebi ne
#    3. seznam naj vsebuje: userje, ki jim ti ne slediš, a oni tebe sledijo


