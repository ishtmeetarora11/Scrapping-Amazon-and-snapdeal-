import requests
from bs4 import BeautifulSoup
class Product:
    def __init__(self,title,price,img,url):
        self.title=title  
        self.price=price
        self.img=img
        self.url=url      
def scrap(query):
    url = "https://www.amazon.in/s"
    params = {"keyword": query}
    r = requests.get(url, params=params)
    url2 = "https://www.snapdeal.com/search"
    params2 = {
    "keyword": query
    }
    r2 = requests.get(url2, params=params2)
    soup = BeautifulSoup(r2.content)
    products_= soup.findAll('div', attrs={"class": "product-tuple-listing"})
    Soup=BeautifulSoup(r.content)
    products=Soup.findAll('div', attrs={"data-index":[i for i in range(15)]})
    results=[]
    for product in products:
        title=product.find('span', attrs={"class": "a-color-base"})
        price=product.find('span', attrs={"class": "a-price-whole"})
        img=product.find('img', attrs={"class": "s-image"})
        if price!=None:
            results.append(Product(title.text,price.text,img.attrs["src"],"amazon"))  
    for product in products_:
        title2=product.find('p', attrs={"class": "product-title"})
        price2=product.find('span', attrs={"class": "product-price"})
        img2=product.find('img', attrs={"class": "product-image"})
        m=price2.text
        if 'src' in img2.attrs:
            results.append(Product(title2.text,m[4:],img2.attrs["src"],"snapdeal"))
        elif 'data-src' in img2.attrs:
            results.append(Product(title2.text,m[4:],img2.attrs["data-src"],"snapdeal"))
    return results        

