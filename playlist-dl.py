#! /usr/bin/python3
# playlist-dl.py - Downloads youtube videos from playlist.

import requests, os, bs4, sys

url = sys.argv[1]
pl = requests.get(url)
ss = requests.get('http://en.savefrom.net/')

pl_soup = bs4.BeautifulSoup(pl.text, "html.parser")
ss_soup = bs4.BeautifulSoup(ss.text, "html.parser")

playlist = pl_soup('#pl-video-table .pl-video-title-link')
ss_linkfield = ss._soup('#sf_url')

for video in playlist:
    vid_url = 'https://youtube.com' + video.attrs['href']
    
