import urllib.request
import bs4 as bs
import re
from selenium import webdriver
from pymongo import MongoClient
import pprint

def scraper(ParentLink):
    visited=[]
    unvisited=[]
    all_tags=[]
    all_tagsNames=[]
    Tags={}
    n=0

    if(ParentLink=="https://slashdot.org/"):
        match="slashdot.org"
        tagDivName='story-tags'
        clName="Slashdot"
        tagAdd='https:'
        
    elif(ParentLink=="https://techcrunch.com/"):
        match='techcrunch.com'
        tagDivName='article__related-links'
        clName="Techcrunch"
        tagAdd='https://techcrunch.com'
        
        
    client=MongoClient('mongodb+srv://RiddhiGupta_05:Nanhi123@learning-in-bits-xoruo.mongodb.net/test?retryWrites=true')
    db=client["Learn-in-Bits-database"]
    collection=db[clName]
    posts=db.posts

    

    driver = webdriver.Chrome('ChromeDriver') 
    website = ParentLink
    driver.get(website) 
    sauce = driver.page_source
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')   
    
    temp_links=body.find_all('a')
    
    for link in temp_links:
        if(link.get('href')!=None and re.search(match,link.get('href')) and re.search('mailto',link.get('href'))==None and re.search('images',link.get('href'))==None):
            unvisited.append(link.get('href'))


    while(len(unvisited)>0 and n<100):
        link=unvisited[0]
        del unvisited[0]

               
        if(link not in visited):
            
            visited.append(link)            

            if(re.search('https:',link)==None and re.search('http:',link)==None):
                link='https:'+link
            
            

            try:
                driver.get(link) 
                link_sauce = driver.page_source
                link_soup=bs.BeautifulSoup(link_sauce,'lxml')
                link_body=link_soup.find('body')
            except IOError:
                print('............................................')
                print(link)
                print('............................................')
                continue


            temp_links=link_body.find_all('a')
            
            for l in temp_links:
                if(l.get('href')!=None and re.search(match,l.get('href')) and re.search('mailto',l.get('href'))==None and (l.get('href') not in visited) and re.search('images',l.get('href'))==None):
                    unvisited.append(l.get('href'))
            
                
            tagDiv=link_body.find_all('div',class_=tagDivName)
            if (tagDiv!=None):
                
                for t in tagDiv:
                    
                    tags=t.find_all('a')
                    for tag in tags:
                        temp=tag.get('href')
                        temp2=tag.text
                        
                        if((temp not in all_tags) and (temp2 not in all_tagsNames) and ((re.search('https:',temp)==None and temp2!='' and ParentLink=="https://techcrunch.com/") or (re.search('slashdot.org',temp) and temp2!='' and ParentLink=="https://slashdot.org/"))):
                            
                            if(re.search('https:',temp)==None and re.search('http:',temp)==None):
                                temp=tagAdd+temp
                            elif(ParentLink=="https://techcrunch.com/"):
                                 temp=tagAdd+temp
                            n+=1
                            all_tags.append(temp)
                            all_tagsNames.append(temp2)
                            #print(temp,"------",temp2)
                            if(posts.find_one({"_id":temp2})==None):
                                post={"TagName":temp2,"TagLink":temp,"_id":temp2}
                                posts.insert_one(post).inserted_id
                                print(post)
                            
                            
                            Tags[temp2]=temp
    '''
    for post in posts.find():
        print("###################")
        pprint.pprint(post)'''

scraper("https://techcrunch.com/")
scraper("https://slashdot.org/")