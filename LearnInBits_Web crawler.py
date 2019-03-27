import urllib.request
import bs4 as bs
import re
from selenium import webdriver
from pymongo import MongoClient



def quoteScraper():
    allLinks=[]
    allTags=[]
    allQoutes=[]

    client=MongoClient('mongodb+srv://RiddhiGupta_05:LearningBits@learning-in-bits-xoruo.mongodb.net/test?retryWrites=true')
    db=client["Learn-in-Bits-database"]
    collection=db['Quotes']
    posts=db.posts
    
    driver = webdriver.Chrome('ChromeDriver') 
    driver.get('https://www.brainyquote.com/topics') 
    sauce = driver.page_source
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')
    
    Links=body.find_all('a')
    for link in Links:
        link=link.get('href')
        if(link!=None and re.search('/topic_index/',link)):
            link='https://www.brainyquote.com'+link
            allLinks.append(link)
            print(link)
    
    for link in allLinks:
        try:
            driver.get(link)
            sauce=driver.page_source
            soup=bs.BeautifulSoup(sauce,'lxml')
        except :
            print("*************************************")
            print(link)
            print("*************************************")
        body=soup.find('body')
        Links=body.find_all('a')
        for l in Links:
            l=l.get('href')
            if(l!=None and (l not in allTags) and re.search('/topics/',l)):
                l='https://www.brainyquote.com'+l
                allTags.append(l)
                print(l)
        
    
    for link in allTags:
        driver.get(link)
        sauce=driver.page_source
        soup=bs.BeautifulSoup(sauce,'lxml')
        body=soup.find('body')
        Boxes=body.find_all('div', class_='qll-bg')
        for b in Boxes:
            l=b.find('a')
            l=l.get('href')
            if(l!=None and re.search('/quotes/',l)):
                l='https://www.brainyquote.com'+l
                allQoutes.append(l)
                print(l)
        

    while(len(allQoutes)!=0):

        quote=allQoutes[0]
        driver.get(quote)
        sauce=driver.page_source
        soup=bs.BeautifulSoup(sauce,'lxml')
        body=soup.find('body')
        
        q=body.find_all('div', class_='quoteContent')
        q=q[0].find('p')
        q=q.text
        tag=body.find_all('div', class_="bqQt bq_s")
        tag=tag[0].find_all('a')
        t=[]
        for temp in tag:
            t.append(temp.text)
        element={'Tags':t,"Quote":q}
        print(element)
        posts.insert_one(element)
        Boxes=body.find_all('div', class_='qll-bg')
        for b in Boxes:
            l=b.find('a')
            l=l.get('href')
            if(l!=None and (l not in allQoutes) and re.search('/quotes/',l)):
                l='https://www.brainyquote.com'+l
                allQoutes.append(l)
        del allQoutes[0]
    

quoteScraper()
