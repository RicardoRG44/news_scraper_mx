📁 Project Structure:


import requests
import urllib3
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

#tell the exact time, simple:)
present=datetime.now()
print(f"{present}\n")


#tell especifyc about the url you whant to use
url = "https://www.eluniversal.com.mx/"

# query the website and return the html to the variable ‘page’
page = requests.get(url)


if page.status_code == 200:
    
    print("The peticion was succesfull")

#parse the html using the method beautifulSoup and store in variable 'soup'
    soup = BeautifulSoup( page.text, 'html.parser')

#found the 'title' and then print the information 
    titletag = soup.find('title')
    print(f'el titulo de la web es: {titletag.string}\n')

#search the HTML in an exact space and store in variable 'textcomplete' 
    textcomplete= soup.find('div', {'class':'opener-chain'})
    
#If found the variable textcomplete, than find all the content 'h2'  
    if textcomplete:
     headers = textcomplete.find_all(['h2'])
     
#order like a table the content
     for header in headers:
         y = json.dumps(header.text.strip(), ensure_ascii=False)
         print(y) 
         
