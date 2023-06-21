# Imports

#standard imports
import pandas as pd
import numpy as np
#import
import unicodedata
#import regular expression operations
import re
#import natural language toolkit
import nltk
#import stopwords list
from nltk.corpus import stopwords


# Imports needed for codeup blog info
import acquire as a
import requests
from requests import get
from bs4 import BeautifulSoup
import os
from pprint import pprint 
import time
import json


def prepare_info():
    print(f'basic_clean(original)')
    print(f'tokenize(basic_cleaned)')
    print(f'remove_stopwords(lemma_or_stem)')
    print(f'stem(clean_tokenize)')
    print(f'lemmatize(clean_tokenize)')





def basic_clean(original):
    '''
    Input: original text or .apply(basic_clean) to entire data frame
    Actions: 
    lowercase everything,
    normalizes everything,
    removes anything that's not a letter, number, whitespace, or single quote
    Output: Cleaned text
    '''
    # lowercase everything
    basic_cleaned = original.lower()
    # normalize unicode characters
    basic_cleaned = unicodedata.normalize('NFKD', basic_cleaned)\
    .encode('ascii', 'ignore')\
    .decode('utf-8')
    # Replace anything that is not a letter, number, whitespace or a single quote.
    basic_cleaned = re.sub(r'[^a-z0-9\'\s]', '', basic_cleaned)
    
    return basic_cleaned




def tokenize(basic_cleaned):
    '''
    Input: basic_cleaned text string or .apply(tokenize) to entire data frame
    Actions:
    creates the tokenizer
    uses the tokenizer
    Output: clean_tokenize text string
    '''
    #create the tokenizer
    tokenize = nltk.tokenize.ToktokTokenizer()
    #use the tokenizer
    clean_tokenize = tokenize.tokenize(basic_cleaned, return_str=True)
    
    return clean_tokenize




def remove_stopwords(lemma_or_stem, extra_words=[], exclude_words=[]):
    '''
    Input:text string or .apply(remove_stopwords) to entire data frame
    Action: removes standard stop words
    Output: parsed_article
    '''
    # save stopwords
    stopwords_ls = stopwords.words('english')
    # removing any stopwords in exclude list
    stopwords_ls = set(stopwords_ls) - set(exclude_words)
    # adding any stopwords in extra list
    stopwords_ls = stopwords_ls.union(set(extra_words))
    
    # split words in article
    words = lemma_or_stem.split()
    # remove stopwords from list of words
    filtered = [word for word in words if word not in stopwords_ls]
    # join words back together
    parsed_article = ' '.join(filtered)
    
    return parsed_article





def stem(clean_tokenize):
    '''
    Inputs: clean_tokenize 
    Actions: creates and uses stemmer for each word
    Outputs: clean_tokenize_stem
    '''
    #create porter stemmer
    ps = nltk.porter.PorterStemmer()
    #use stemmer - apply stem to each word in our string
    stems = [ps.stem(word) for word in clean_tokenize.split()]
    #join words back together
    clean_tokenize_stem = ' '.join(stems)
    
    return clean_tokenize_stem





def lemmatize(clean_tokenize):
    '''
    Inputs: clean_tokenize
    Actions: creates lemmatizer and applies to each word
    Outputs: clean_tokenize_lemma
    '''
    #create the lemmatizer
    wnl = nltk.stem.WordNetLemmatizer()
    #use lemmatize - apply to each word in our string
    lemmas = [wnl.lemmatize(word) for word in clean_tokenize.split()]
    #join words back together
    clean_tokenize_lemma = ' '.join(lemmas)
    
    return clean_tokenize_lemma






