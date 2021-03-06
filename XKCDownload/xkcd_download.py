#!/usr/bin/python

# Disclaimer: This script is only for educational purposes.
# Please use this at your own risk.
# Author: jsinix(jsinix.1337@gmail.com) 

# This script is used to dowload all the indexed images from XKCD(http://www.xkcd.com). 
# I am checking some expected errors, but it is very much possible that some erros may 
# occur for someone using. 

import requests, sys, re
from bs4 import BeautifulSoup
import urllib, urlparse, os.path 

url1 = "http://xkcd.com/"
collect_url = []

def get_image_url(uri01):
    r = requests.get(uri01)
    soup = BeautifulSoup(r.content)
    g_data = soup.find_all("div", {"class": "box"})
    interest =  g_data[2].contents[5]
    interest = str(interest)
    from_interest = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', interest)
    for jj in from_interest:
        collect_url.append(jj)

def download_url(uri02):
    file1 = urllib.URLopener()
    path = urlparse.urlparse(uri02).path
    fn = os.path.split(path)[-1]
    file1.retrieve(uri02, fn)

def max_range(uri03):
    r = requests.get(uri03)
    soup = BeautifulSoup(r.content)
    g_data = soup.find_all("ul", {"class": "comicNav"})
    some = g_data[0]
    dos = []
    for link in some.find_all("a"):
        dos.append(link.get("href"))
    word1 = dos[1]
    word2 = word1[1:-1]
    word2 = int(word2)
    return word2

def controller():
    upper_limit = max_range(url1)    
    try: 
	sys.stdout.write('\rParsing: ' + url1)
	sys.stdout.flush()
        get_image_url(url1)
    except:
        print "\nParse error: %s" % url1    

    for tailer in range(1,upper_limit):
        try:
	    current_url = url1+str(tailer)+"/"
	    sys.stdout.write('\rParsing: ' + current_url)
            sys.stdout.flush()
            get_image_url(current_url)
        except: 
            print "\nParse error: %s" % current_url

    for iLink in collect_url:        
	try: 
	    sys.stdout.write('\rDownloading: ' + iLink)
	    download_url(iLink)
        except:
	    print "\nDownload error: %s" % iLink    

if __name__ == '__main__':
    print Welcome
    print Disclaimer
    controller()
