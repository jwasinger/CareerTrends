#! ./.env/bin/python

from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen('http://python.org')
html = response.read()

soup = BeautifulSoup(html)
print soup.head
