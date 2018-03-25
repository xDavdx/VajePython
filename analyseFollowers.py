from bs4 import BeautifulSoup
import codecs

fileing = codecs.open("following.html", 'r', 'utf-8')
fileers = codecs.open("followers.html", 'r', 'utf-8')

followingHTML = fileing.read()
followersHTML = fileers.read()

souping = BeautifulSoup(followingHTML, 'html.parser')
soupers = BeautifulSoup(followersHTML, 'html.parser')

following = []
for one in souping.find_all("a", attrs={"class": "_2g7d5 notranslate _o5iw8"}):
    following.append(one.string)

followers = []
for one in soupers.find_all("a", attrs={"class": "_2g7d5 notranslate _o5iw8"}):
    followers.append(one.string)

# Naloga: 
# Zgradi tri sezname: 
#    1. seznam naj vsebuje: userje, ki jim slediš in oni tudi tebi
#    2. seznam naj vsebuje: userje, ki jim slediš in oni tebi ne
#    3. seznam naj vsebuje: userje, ki jim ti ne slediš, a oni tebe sledijo




