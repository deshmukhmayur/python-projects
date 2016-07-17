#/usr/bin/python3

import requests, os
from bs4 import BeautifulSoup

def download(url):
    print ('Opening %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    print ('Saving the file: %s...' % os.path.basename(url))
    file = open(os.path.basename(url), 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()

homepage = 'http://bamua.digitaluniversity.ac'

print ('Opening %s...' % homepage)
result = requests.get(homepage)
result.raise_for_status()

soup = BeautifulSoup(result.text, "html.parser")
links = soup.select('#UCDownloads .downloadsTD')

print ('Searching for downloads...')
for item in links:
    if "S.E." in item.text:
        download(item.attrs['href'])
        break

print ('Download complete.')
