from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from .models import Requete,Article

def cree_fich(email) :
    Req=Requete.objects.all()
    Req_imp=[]
    date = ''
    for reqs in Req :
        if reqs.Email==email :
            Req_imp.append(reqs.requete)
    for requets in Req_imp :
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://scholar.google.com/")
        search = driver.find_element_by_name("q")
        search.send_keys(requets)
        search.send_keys(Keys.RETURN)
        url = driver.current_url
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
        link = []
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, features="html.parser")
        i = 0
        for abc in soup.find_all(id='gs_bdy_sb_in'):
            for abc1 in abc.find_all('li', class_='gs_ind'):
                for abc2 in abc1.find_all('a'):
                    i += 1
                    if (i == 7): link.append('https://scholar.google.com' + abc2['href'])
        response = requests.get(link[0], headers=headers)
        soup = BeautifulSoup(response.text, features="html.parser")
        for i in range(len(soup.select('div#gs_nml>a'))):
            link.append('https://scholar.google.com' + soup.select('div#gs_nml>a')[i]['href'])
        k = 0
        for lin in link:
            response = requests.get(lin, headers=headers)
            soup = BeautifulSoup(response.text, features="html.parser")
            for item in soup.find_all('div', class_='gs_r gs_or gs_scl'):
                nv_article = Article()
                nv_article.Email = email
                j = 0
                tour = 0
                for i in item.find_all('a'):

                    if (j == 0):
                        if ('[PDF]' in i.get_text()):
                            nv_article.lien_document=i['href']
                            #print('Pdf :' + i['href'])
                            j += 1
                        elif ('[HTML]' in i.get_text()):
                            j += 1
                        elif ('[DOC]' in i.get_text()):
                            nv_article.lien_document = i['href']
                            #print('Doc :' + i['href'])
                            j += 1
                        else:
                            if ("https://" in i['href'] or "http://" in i['href']):
                                nv_article.lien_site = i['href']
                                nv_article.titre_article = i.get_text()
                                #nv_article.date_article = item.find('div', class_='gs_rs').get_text()
                                nv_article.lien_document = " n'existe pas "
                                date = item.find('span', class_='gs_age').get_text()
                                #print('link :' + i['href'])
                                #print('Title :' + i.get_text())
                                #print(item.find('span', class_='gs_age').get_text())
                                #print(item.find('div', class_='gs_rs').get_text())
                                j += 2
                    elif (j == 1 and tour == 1):
                        if ('/scholar?output' in i['href']):
                            j += 1
                        else:
                            if ("https://" in i['href'] or "http://" in i['href']):
                                nv_article.lien_site = i['href']
                                nv_article.titre_article = i.get_text()
                                #nv_article.date_article = item.find('div', class_='gs_rs').get_text()

                                date = item.find('span', class_='gs_age').get_text()
                                #print('link :' + i['href'])
                                #print('Title :' + i.get_text())
                                #print(item.find('span', class_='gs_age').get_text())
                                #print(item.find('div', class_='gs_rs').get_text())
                                j += 2
                    tour += 1
                    #print('\n\n')
                x=(int)(date.split())[3]

                if(x<10) :
                    nv=0 #article n'existe pas
                    T_article=Article.objects.all()
                    T_article_email=[]
                    for art in T_article :
                        if(art.Email==email) :
                            T_article_email.append(art)
                    for arts in T_article_email :
                        if(arts.titre_article==nv_article.titre_article) :
                            nv=1
                    if(nv==0) :
                        nv_article.nouveau='nv'
                        nv_article.save()
        driver.quit()


