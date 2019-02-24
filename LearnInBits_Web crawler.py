import urllib.request
import bs4 as bs
import re

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
        if(unvisited[0] not in visited):
            link=unvisited[0]
            visited.append(link)

            if(re.search('https:',link)==None and re.search('http:',link)==None):
                link='https:'+link
            

            try:
                link_sauce=urllib.request.urlopen(link).read()
                link_soup=bs.BeautifulSoup(link_sauce,'lxml')
                link_body=link_soup.find('body')
                temp_links=link_body.find_all('a')
                for l in temp_links:
                    if(l.get('href')!=None and re.search('slashdot.org',l.get('href')) and re.search('mailto',l.get('href'))==None and (l.get('href') not in visited) and re.search('images',l.get('href'))==None):
                        unvisited.append(l.get('href'))
            except:
                print('............................................')
                print(link)
                print('............................................')
                continue
                
            tagDiv=link_body.find_all('div',class_='story-tags')
            if (tagDiv!=None):
                for t in tagDiv:
                    tags=t.find_all('a')
                    for tag in tags:
                        temp=tag.get('href')
                        temp2=tag.text
                        if((temp not in all_tags) and re.search('slashdot.org',temp)):
                            if(re.search('https:',temp)==None and re.search('http:',temp)==None):
                                temp='https:'+temp
                            all_tags.append(temp)
                            all_tagsNames.append(temp2)
                            Tags[temp2]=temp
            
            
            
        del unvisited[0]

slashdot_scraper()


