# web scraping 

import requests
from bs4 import BeautifulSoup as bs

name=input("enter any github user name")
url="https://github.com/"+name
page=requests.get(url)
soup=bs(page.content,"html.parser")

#image=soup.findAll('img')
imager=soup.find("img",class_="avatar avatar-user width-full border color-bg-primary")
print(imager['src'])

repo_cnt=soup.find("span",class_="Counter")
print("Total repositories of user {} is {}".format(name,repo_cnt['title']))

#print(soup)
repo_lst=soup.find_all('span',class_="repo")
#print(repo_lst)
print("list of repositories are:")
for i in repo_lst:
    print(type(i))
    print(i['title'])

