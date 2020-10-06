import re, requests
from bs4 import BeautifulSoup
import webbrowser




animelist = [
    "Majo no Tabitabi",
    "100-man no Inochi no Ue ni Ore wa Tatteiru",
    "Tonikaku Kawaii",
    "Munou na Nana",
    "Kamisama ni Natta Hi",
    "Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen"
]


def rename():
    global animelist
    for anime in animelist:
        temp = anime
        anime = temp.replace(" ","+")
        



def getMagnets(anime):
    nyaa_link = 'https://nyaa.si/?f=0&c=1_2&q='+ anime
    request = requests.get(nyaa_link, headers={'User-Agent': 'Mozilla/5.0'})
    source = request.content
    soup = BeautifulSoup(source, 'lxml')

    #GETTING TORRENT NAMES
    #GETTING TORRENT NAMES
    title = []
    rows = soup.findAll("td", colspan="2")
    for row in rows:
        desired_title = row.text.strip().split('\n')[-1]
        title.append(desired_title)
    #print(title)
    pos= getPosition(title)

    #GETTING MAGNET LINKS
    magnets = []
    for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
        magnets.append(link.get('href'))
    #print(magnets)

    #GETTING NUMBER OF MAGNET LINKS AND TITLES
    #print('Number of magnet links', len(magnets))
    #print('Number of titles', len(title))
    #print(magnets[pos])
    return magnets[pos]



def getPosition(titlelist):
    tracker=0
    position=0
    for title in titlelist:
        
        if title.find("720p") != -1:
            
            position=tracker
            return position
        tracker+=1
    
    

links = []

if __name__ == "__main__":
    rename()
    for anime in animelist:
        try:
            links.append(str(getMagnets(anime)))
        except:
            pass
            
        
    for i in links:
        print(i)
        webbrowser.open(i)
    
    

    











