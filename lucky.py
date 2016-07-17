#! python3
# lucky.py - Opens several google search results.

import sys, requests, webbrowser, bs4, pyperclip

if len(sys.argv) > 1:
    search = sys.argv[1:]
else:
    search = pyperclip.paste().split()

print ('Googling...')
res = requests.get('http://google.com/search?q=' + '+'.join(search))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    
