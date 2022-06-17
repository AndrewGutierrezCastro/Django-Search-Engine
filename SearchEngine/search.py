import requests
from bs4 import BeautifulSoup
from WebSpiderRIT.Query import query

# done
def google(s):
    links = []
    text = []
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    headers = {"user-agent": USER_AGENT}
    r = requests.get("https://www.google.com/search?q=" + s, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    for g in soup.find_all('div', class_='yuRUbf'):
        a = g.find('a')
        t = g.find('h3')
        links.append(a.get('href'))
        text.append(t.text)
    return links, text


#Grupo 3 Model
def oursearchengine(s):
    links = []
    text = []
    documents, metrics = query(s)
    for document in documents:
        links.append(document["URL_Producto"])
        text.append(document["Desc_Producto"])
    print(metrics)
    return links, text
