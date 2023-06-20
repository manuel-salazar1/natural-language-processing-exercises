# Imports

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint 
import time




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






