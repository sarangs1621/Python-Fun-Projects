from bs4 import BeautifulSoup as BS
import requests

def get_price(url):
   data=requests.get(url)
   soup=BS(data.text,'html.parser')
   ans=soup.find('div',id='current-price').text
   return ans
url='https://www.goodreturns.in/gold-rates/'
ans=get_price(url)
print(ans)
