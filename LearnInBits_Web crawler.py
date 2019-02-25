import urllib.request
import bs4 as bs
import re
from selenium import webdriver

def slashdot_scraper():
    visited=[]
    unvisited=[]
    all_tags=[]
    all_tagsNames=[]
    Tags={}
    sauce=urllib.request.urlopen("https://slashdot.org/").read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')   
    
    temp_links=body.find_all('a')
    for link in temp_links:
        if(link.get('href')!=None and re.search('slashdot.org',link.get('href')) and re.search('mailto',link.get('href'))==None and re.search('images',link.get('href'))==None):
            unvisited.append(link.get('href'))


    while(len(unvisited)>0):
        link=unvisited[0]
        del unvisited[0]

        if(link not in visited):
            
            visited.append(link)            

            if(re.search('https:',link)==None and re.search('http:',link)==None):
                link='https:'+link
            
            

            try:
                link_sauce=urllib.request.urlopen(link).read()
                link_soup=bs.BeautifulSoup(link_sauce,'lxml')
                link_body=link_soup.find('body')
            except:
                print('............................................')
                print(link)
                print('............................................')
                continue


            temp_links=link_body.find_all('a')
            for l in temp_links:
                if(l.get('href')!=None and re.search('slashdot.org',l.get('href')) and re.search('mailto',l.get('href'))==None and (l.get('href') not in visited) and re.search('images',l.get('href'))==None):
                    unvisited.append(l.get('href'))
            
                
            tagDiv=link_body.find_all('div',class_='story-tags')
            if (tagDiv!=None):
                for t in tagDiv:
                    tags=t.find_all('a')
                    for tag in tags:
                        temp=tag.get('href')
                        temp2=tag.text
                        
                        if((temp not in all_tags) and (temp2 not in all_tagsNames) and re.search('slashdot.org',temp) and temp2!=''):
                            if(re.search('https:',temp)==None and re.search('http:',temp)==None):
                                temp='https:'+temp
                            all_tags.append(temp)
                            all_tagsNames.append(temp2)
                            Tags[temp2]=temp
                            


def techcrunch_scraper():
    visited=[]
    unvisited=[]
    all_tags=[]
    all_tagsNames=[]
    Tags={}
    driver = webdriver.Chrome('C:\\Users\\mailr\\Desktop\\ChromeDriver') 
    website = "https://techcrunch.com/"
    driver.get(website) 
    sauce = driver.page_source   
    #sauce=urllib.request.urlopen("https://techcrunch.com/").read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')
    temp_links=body.find_all('a')
    
    for link in temp_links:
        if(link.get('href')!=None and re.search('techcrunch.com',link.get('href')) and re.search('mailto',link.get('href'))==None and re.search('images',link.get('href'))==None):
            unvisited.append(link.get('href'))
    
    
    while(len(unvisited)>0):
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
            except:
                print('............................................')
                print(link)
                print('............................................')
                continue


            temp_links=link_body.find_all('a')
    
            for l in temp_links:
                if(l.get('href')!=None and re.search('techcrunch.com',l.get('href')) and re.search('mailto',l.get('href'))==None and (l.get('href') not in visited) and re.search('images',l.get('href'))==None):
                    unvisited.append(l.get('href'))
            
                
            tagDiv=link_body.find_all('div',class_='article__related-links')
            
            if (tagDiv!=None):
                
                for t in tagDiv:
                    
                    tags=t.find_all('a')
                    for tag in tags:
                        temp=tag.get('href')
                        temp2=tag.text
                        
                        if((temp not in all_tags) and (temp2 not in all_tagsNames) and re.search('https:',temp)==None and temp2!=''):
                            temp='https://techcrunch.com'+temp
                            all_tags.append(temp)
                            all_tagsNames.append(temp2)
                            Tags[temp2]=temp
