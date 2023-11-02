'''Dashboard em python
Criado por: Ilton Batista
Data de inicio: 31/10/2023
Proposito: Desenvolver habilidades de raciocinio e experiencia com novas bibliotecas de analise de dados e dashboard
'''

import requests
from bs4 import BeautifulSoup



def get_news():
    url = 'https://globo.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    noticias = soup.find_all('a') # busca todas as tag A
    tgt_class1 = 'post__title'
    tgt_class2 = 'post-multicontent__link--title__text'

    news_dict = {}
    for noticia in noticias:
        if (noticia.h2 != None) and (noticia.h2.get('class') != None):
            if tgt_class1 in noticia.h2.get('class'):
                news_dict[noticia.h2.text] = noticia.get('href')
            if tgt_class2 in noticia.h2.get('class'):
                news_dict[noticia.h2.text] = noticia.get('href')
    return news_dict


news = get_news()
len(news)
list(news.keys())[30]

