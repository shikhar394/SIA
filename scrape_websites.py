from bs4 import BeautifulSoup
import requests
import sys  

def scrape_websites(url):
  #url = raw_input("Enter a website to extract the URL's from: ")

  r  = requests.get("http://" +url)

  data = r.text

  soup = BeautifulSoup(data)

  for link in soup.find_all('a'):
      link_from_web=link.get('href')
      #if 'major' in link_from_web:
      print(link_from_web)


if __name__ == "__main__":
  print(sys.argv)
  if len(sys.argv)>1:
    scrape_websites(sys.argv[1])