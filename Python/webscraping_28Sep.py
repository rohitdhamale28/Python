# webscraping 

#pip install requests

#pip install bs4   (beautifulsoup)


# webscraping is used to read data from a public website n use it in our python program 
# libaries : 1. beautifulsoup 2.scraping

# https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture 
# using the above link to extract data 



#-------------------------------------------------------------------------------------

import requests  
from bs4 import BeautifulSoup
import re
#https://en.wikipedia.org/

headers = {
    "User-Agent": "MyWikipediaBot/1.0 (contact@example.com) Python-requests"
}

url = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
response = requests.get(url,headers=headers)
type(response) # requests.models.Response
print(response.text)


# converting response to object of class BeautifulSoup  
#[ requests.models.Response --> bs4.BeautifulSoup ]
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)  #  bs4.BeautifulSoup : object of class BeautifulSoup is created
print(html_soup)

award_list=html_soup.find_all("tr",{"style":'background:#FAEB86'})
print(len(award_list))

first_award=award_list[0]
print("*"*80)
print(first_award)

val=first_award.find("a",{"href":re.compile("film\)")}).get("href")
print(val)

#other way to retrieve href data

data=first_award.find("a",{"href":re.compile("film\)")})
print(data.text)
val1=data["href"]
print(val1)

#https://en.wikipedia.org/wiki/Wings_(1927_film)
newurl="https://en.wikipedia.org"+val
print(newurl)
newresponse = requests.get(newurl,headers=headers)
print(newresponse.text)
newdata=BeautifulSoup(newresponse.text,"html.parser")

title=newdata.select("h1[id='firstHeading'] i")[0].text
#other way to do the same above func
title1=newdata.select_one("h1[id='firstHeading'] i").text
print(title)
print(title1)

arr=newdata.select("tr:-soup-contains('Directed by') a[href*='/wiki/']")
title=arr[0].text
title1=newdata.select_one("tr:-soup-contains('Directed by') a[href*='/wiki/']").text
print(title)
print(title1)

title=newdata.select("tr:contains('Release dates') li")[0].text
title1=newdata.select_one("tr:contains('Release dates') li").text
print(title)
print(title1)

#data['title']=response.css(r"h1[id='firstHeading'] i::text").extract()
#data['directedby']=response.css(r"::text").extract()
#data['starring']=-----
#data['releasedate']=response.css(r"::text").extract()

names=[]
directedby=[]
releaseddate=[]
for movie in award_list:
    data=movie.find("a",{"href":re.compile("film\)")})
    if data!=None:
        val=data["href"]
        newurl="https://en.wikipedia.org"+val
        print(newurl)
        newresponse = requests.get(newurl)
        newdata=BeautifulSoup(newresponse.text,"html.parser")
        title=newdata.select_one("h1[id='firstHeading'] i")
        if title!=None:
            names.append(title.text)
        else:
            names.append("")
        director=newdata.select("tr:-soup-contains('Directed by') a[href*='/wiki/']")[0].text
        directedby.append(director)
        releasedt=newdata.select_one("tr:contains('Release dates') li")
        if releasedt!=None:
            releaseddate.append(releasedt.text)
        else:
            releaseddate.append("")
d={"title":names,"directedby":directedby,"releaseddate":releaseddate}
import pandas as pd
df=pd.DataFrame(d)
print(df.head())
    




