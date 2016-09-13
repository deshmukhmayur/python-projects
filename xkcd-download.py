#! /usr/bin/python3
# download.py - Downloads every single XKCD comic.

import requests, os, bs4, sys

def main(startFrom=''):
    try:
        '''Downloads all the comics from XKCD.'''
        url = 'http://xkcd.com/' + str(startFrom)       #starting url
        os.makedirs('xkcd', exist_ok=True)              #stores comics in ./xkcd

        retry_no = 0
        while not url.endswith('#'):
            #Download the page.
            print ('Opening the page %s...' % url)
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, "html.parser")

            #Find the url of the comic image.
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print ('Could not find comic image.')
            else:
                try:
                    comicUrl = 'http:' + comicElem[0].get('src')
                    name = os.path.basename(comicUrl)
                    for fileName in os.listdir('xkcd'):
                        if fileName == name:
                            raise RuntimeError()
                    else:
                        # Download the image.
                        print ('Loading the image %s...' % (comicUrl))
                        res = requests.get(comicUrl)
                        res.raise_for_status()
                except requests.exceptions.ConnectionError:
                    # retry
                    if retry_no < 3:
                        retry_no += 1
                        print ('Download failed. Trying again...')
                        print ('Retry Attempt: %d' % retry_no)
                        continue
                    else:
                        print ('DownloadError: Skipping file %s' % name)
                except requests.exceptions.MissingSchema:
                    # skip this comic
                    print ('Error MissingSchema for %s' % name)
                except RuntimeError:
                    # it already exists
                    print ('File already exists: %s' % name)
                else:
                    # Save the image to ./xkcd.
                    imageFile = open(os.path.join('xkcd', name), 'wb')
                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
                    byteSize = len(res.content)
                    size = round(byteSize / 1024, 2)
                    print ('Downloaded image %s... (%.2f KB)' % (name, size))

            # Get the Prev button's url
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            retry_no = 0

    except KeyboardInterrupt:
        print ('Terminating Download.')
    finally:
        print ('Done.')
        if imageFile:
            imageFile.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
