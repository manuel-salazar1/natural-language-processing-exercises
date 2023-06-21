# Imports

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint 
import time
import json


def acquire_info():
    '''
    I always forget what exactly is in each .py file
    This function will remind me when the time comes :)
    '''
    print(f'get_blog_articles2()')
    print(f'scrape_one_page(topic)')
    print(f'get_news_articles(topic_list)')



def get_blog_articles(response):
    '''
    Input:'response', follow steps below to get response
    url = 'https://codeup.com/blog/'
    headers = {"User-Agent": "Chrome/91.0.4472.124"}
    response = get(url, headers=headers)
    Output: blog_stuff 
    list of dictionaries
    blog_stuff = get_blog_articles(response)
    '''
    soup = BeautifulSoup(response.content, 'html.parser')
    blog_stuff = []
    for element in soup.find_all(class_='entry-title'):
        # print(element)
        one_blog = {}
        one_blog['title'] = element.find('a').text
        url = element.find('a')['href']
        headers = {"User-Agent": "Chrome/91.0.4472.124"}
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('div', class_="entry-content")
        one_blog['content'] = article.text
        blog_stuff.append(one_blog)
    return blog_stuff




def get_blog_articles2(article_list):
    '''
    Input: link_list
    example:
    url = "https://codeup.com/blog/"
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    more_links = soup.find_all('a', class_='more-link')
    links_list = [link['href'] for link in more_links]
    Output: article_info and json
    '''
    file = 'blog_posts.json'
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
    
    headers = {'User-Agent': 'Codeup Data Science'}
    article_info = []
    
    for article in article_list:
        
        response = get(article, headers = headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        info_dict = {"title":soup.find('h1').text,
                    'link': link,
                    'date_published': soup.find('span', class_='published').text,
                    'content': soup.find('div', class_='entry-content').text}
        
        article_info.append(info_dict)
     
    with open(file, 'w') as f:
        json.dump(article_info, f)
    return article_info






# -----------------------------------------------------------------------

def scrape_one_page(topic):
    '''
    Input: Topic from website i.e. Business, Technology, etc.
    Output: Summary list
    '''
    
    #topic = "business"
    base_url = "https://inshorts.com/en/read/"
    
    response = get(base_url + topic)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.find_all('span', itemprop='headline')
    
    summaries = soup.find_all('div', itemprop='articleBody')
    
    summary_list = []
    
    for i in range(len(titles)):
        temp_dict = {'category': topic,
                    'title': titles[i].text,
                    'content': summaries[i].text}
        summary_list.append(temp_dict)
    return summary_list










def get_news_articles(topic_list):
    '''
    Input: topic_list
    Output: final_list
    '''
    file = 'news_articles.json'
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
        
    final_list = []
    
    for topic in topic_list:
        final_list.extend(scrape_one_page(topic))
    
    with open(file, 'w') as f:
        json.dump(final_list, f)
    return final_list



