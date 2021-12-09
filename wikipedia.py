import requests
from bs4 import BeautifulSoup
import lxml

#this function calculates the number of 3, 4 and 5-letter words in a given paragraph

    

def scrape_article(url):
    response = requests.get(url = url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.findAll('p')
    words_3 = 0
    words_4 = 0
    words_5 = 0
    count_paragraphs = 0
    for paragraph in paragraphs:
        para = paragraph.text
        words_3 += len([word for word in para.split() if len(word) == 3])
        words_4 += len([word for word in para.split() if len(word) == 4])
        words_5 += len([word for word in para.split() if len(word) == 5])
        count_paragraphs += 1
    
    perpara_3 = int(words_3/count_paragraphs)
    perpara_4 = int(words_4/count_paragraphs)
    perpara_5 = int(words_5/count_paragraphs)

    print("3-letter words: {}/paragraph. \n4-letter words: {}/paragraph. \n5-letter words: {}/paragraph.".format(perpara_3, perpara_4, perpara_5))

url = input("Enter Wikipedia page?")
print("Scraping started")
scrape_article(url)