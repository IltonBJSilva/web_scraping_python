'''Web Scraping em python

Criado por: Ilton Batista

Data de inicio: 31/10/2023

Proposito: Desenvolver habilidades de raciocinio e experiencia com novas bibliotecas de analise de dados e dashboard
'''

# Importar as bibliotecas
import requests
from bs4 import BeautifulSoup
import json



# Função para buscar as noticias do site globo.com
# Retornar um dicionario com as noticias e os links
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


len(get_news()) # quantidade de noticias
list(news.keys()) # lista de noticias

news = get_news() # dicionario de noticias armazenado em uma variavel


# Escolher o nome do arquivo
nome_arquivo = input('Escolha o nome do Arquivo:') 

# Conteúdo que queremos escrever no arquivo
#conteudo = str(list((get_news()).keys()))


# Criar o arquivo no modo de escrita ("w") e escrever o conteúdo no arquivo criado em json
try:

    # Abrir o arquivo no modo de escrita ("w")

    with open(nome_arquivo+'.json', "w") as arquivo:

        json.dump(news, arquivo, indent=4)
        # Escrever o conteúdo no arquivo
        #arquivo.write(news)


    # Arquivo criado com sucesso

    print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")
# Tratar a exceção se o arquivo não for encontrado
except FileNotFoundError:

    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
# Tratar a exceção se não tivermos permissão para escrever o arquivo
except PermissionError:

    print(f"Você não tem permissão para criar o arquivo '{nome_arquivo}'.")
# Tratar a exceção genérica
except Exception as e:

    print(f"Ocorreu um erro inesperado: {e}")