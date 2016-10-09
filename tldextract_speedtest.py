# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 22:41:47 2016

Simple script to check if lexical scoping, explicit passing, or partial is faster
@author: Zeyi
"""

import pandas as pd
import timeit
import tldextract
from functools import partial

no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)

def extract_domain(url):
    a = no_fetch_extract(url)
    return '.'.join([x for x in a if x])

def partial_ext_dom(url, parser):
    a = parser(url)
    return '.'.join([x for x in a if x])

if __name__ == "__main__":
    a = pd.read_csv('alexaSG500.csv', names=['index','host'], usecols=['host'])
    
    timeit.timeit("a['host'].apply(extract_domain)", number=30)
    
    partialfun = partial(partial_ext_dom, parser=tldextract.TLDExtract(suffix_list_urls=None))
    timeit.timeit("a['host'].apply(partialfun)", number=30)
    
    timeit.timeit("a['host'].apply(extract_domain, args=(no_fetch_extract,))", number=30)
    
    
    
    