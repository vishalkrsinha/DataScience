# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:41:48 2018

@author: vk4cs
"""

import bs4, requests

def getAmazonProductPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()   
    soup = bs4.BeautifulSoup(res.text,"lxml")
    soup.select('#usedOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    elements = soup.select('#usedOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')    
    return elements[0].text.strip()

price = getAmazonProductPrice('http://www.amazon.com/Automate-Boring-Python-Albert-Sweigart/dp/1593275994/ref=sr_1_1?s=books&ie=UTF8&qid=1536291470&sr=1-1&keywords=automate+the+boring+stuff+with+python')
print('The price of product is: '+ price)