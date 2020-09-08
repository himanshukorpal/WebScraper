import requests #Download intially html
from bs4 import BeautifulSoup #allows us to use html and grab different data
import pprint
url = 'https://news.ycombinator.com/news?p=' + '1'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
morelinks = soup.select('.morelink')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True) # sorting dictionary by key

def create_custom_hn(links, subtext):
    hn = list()
    for indx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None) # None is default in case their is no href
        vote = subtext[indx].select('.score')

        if len(vote):
            points =int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link' : href, 'votes' : points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
pprint.pprint(morelinks)



