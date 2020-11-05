#   store novel into a txt file
#   function：change the page_numbers will change the chapter you want to recieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import re
main_websites = "https://www.uukanshu.com/b/1229/"
page_numbers = 48331 #this is the first chapter for this novel on this site
url_ending = ".html"
html = urlopen(
    main_websites + str(page_numbers) + url_ending
).read().decode('GBK') #GBK: decode into chinese

soup = BeautifulSoup(html, features = "html.parser") #parse website
content = soup.find_all('div',{"id":"contentbox"})
novel = content[0].get_text() #its content

title = soup.find_all("h1",{"id":"timu"}) #its title
f = open("novel.txt", "a") #append into novel.txt
f.write(title[0].get_text() +"\n")
for i in novel:
    f.write(i)
f.close()

""" 
#if you want to have more that one chapter, then use this loop change the 10 to actual chapter you want to recieve
for i in range(10): 
    page_numbers += 1
    html = urlopen(
        main_websites + str(page_numbers) + url_ending
    ).read().decode('GBK') #GBK: decode into chinese

    soup = BeautifulSoup(html, features = "html.parser") #parse website
    content = soup.find_all('div',{"id":"contentbox"})
    novel = content[0].get_text() #its content

    title = soup.find_all("h1",{"id":"timu"}) #its title
    f = open("novel.txt", "a")
    f.write(title[0].get_text() +"\n")
    for i in novel:
        f.write(i)
    f.write("\n\n")
    f.close()
"""