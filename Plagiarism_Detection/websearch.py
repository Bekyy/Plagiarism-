import requests
from bs4 import BeautifulSoup as bs
import warnings
import re

warnings.filterwarnings("ignore", module='bs4')

def searchBing(query, num):

    url = 'https://www.bing.com/search?q=' + query
    # url = 'https://int.search.myway.com/search?q=' + query
    urls = []

    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    headers = { 'User-Agent': User_Agent}

    # send requests
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'html.parser')
    a_tags = soup.find_all('a')

    for link in a_tags:
        url = str(link.get('href'))
        if url.startswith('http'):
            if not url.startswith('http://go.m') and not url.startswith('https://go.m'):
                urls.append(url)
        
    return urls[:num]
        # results = []
    #     for g in soup.find_all('div', class_='r'):
    #         anchors = g.find_all('a')
    #         if anchors:
    #             link = anchors[0]['href']
    #             title = g.find('h3').text
    #             item = {
    #                 "title": title,
    #                 "link": link
    #                 }
    #                 results.append(item)
    # return results               


def extractText(url):
    page = requests.get(url)
    # Get elements and extract text content.
    soup = bs(page.text, 'html.parser')
    # soup.find('p').get_text()
    return soup.get_text()
    
