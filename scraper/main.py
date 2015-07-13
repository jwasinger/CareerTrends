#! ./.env/bin/python

from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen('http://python.org')
html = response.read()

soup = BeautifulSoup(html)
print soup.head

class JobListing:
  Title = ''
  Location = ('', '') #(city, country)
  Description = ''
  Perks = []
  Tags = []



def get_jobs(keywords, location, distance, distance_units):
  jobs = []

  #parse arguments and create the link to scrape from
  url_str = __create_link_url(keywords, location, distance, distance_units)

  #make the HTTP request
  response = urllib2.urlopen(url_str)
  html = response.read()
  soup = BeautifulSoup(html)
  
  #parse the html

def __create_link_url(keywords, location, distance, distance_units):
  url_str = 'http://careers.stackoverflow/jobs'
  if keywords: 
    url_str += '&keywords='+keywords.replace(' ', '+') #encode spaces on location string

  if location:
    url_str += '&location='+location.replace(' ', '+') #encode spaces on location string
  
  if distance: 
    url_str += '&distance='+distance
  
  if distance_units:
    url_str += '&distanceUnits='+distance_units

  return url_str

def __parse_http_response(soup):
  #for now parse first page of response jobs
  
