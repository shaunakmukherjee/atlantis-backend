
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

def get_repository():
    base_url = "https://github.com/vinta/awesome-python"
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Error in fetching!")
        return
    else:
        print(response.status_code)
        
        ramen = BeautifulSoup(response.content, 'lxml')
        all_links = ramen.find_all('a', attrs={'href': re.compile("^https://")}) #trying to find links especially with the HTTPS and avoiding relative links 
        set_of_links = []
        set_of_names = []
        for i, link in enumerate(all_links):
            every_link = link.get('href')
            every_name = link.text
            set_of_links.append(every_link) #both these lists are initialized during runtime
            set_of_names.append(every_name)

        #print(set_of_names)
        print("Repository scraped! \n")
        query = input("Enter query here -> ")
        if query in set_of_names:
            print(set_of_links[set_of_names.index(query)])
        else:
            query = query.lower() #since most of the links are in lowercase, this is a necessary check but just once
            if query in set_of_names:
                print(set_of_links[set_of_names.index(query)])
            else:
                print("Not in the system!")

if __name__=="__main__":
    print("Scraping started")
    get_repository()