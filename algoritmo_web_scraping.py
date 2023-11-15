from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re
todos_dados = [] # variavel pra armazenar todos os dados e consumir toda memorio do meu computador

navegador = webdriver.Edge()

navegador.get('https://veiculos.fipe.org.br/')

navegador.find_element('xpath', '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a').click()

sleep(2)

navegador.find_element('xpath', '//*[@id="selectTabelaReferenciacarro"]').click()

sleep(2)

site = BeautifulSoup(navegador.page_source, 'lxml')


anos = site.find(id='selectTabelaReferenciacarro').find_all('option')
marcas = site.find(id='selectMarcacarro').find_all('option')

for i in range(1, len(anos) + 1):
    navegador.find_element('xpath', f'//*[@id="selectTabelaReferenciacarro"]/option[{i}]').click()
    sleep(1)

    for j in range(2, len(marcas) + 1):
        navegador.find_element('xpath', f'//*[@id="selectMarcacarro"]/option[{j}]').click()
        sleep(1)
        site = BeautifulSoup(navegador.page_source, 'lxml')

        ano_modelo = site.find(id='selectAnoModelocarro').find_all('option')

        for k in range(2, len(ano_modelo) + 1):
            navegador.find_element('xpath', f'//*[@id="selectAnoModelocarro"]/option[{k}]').click()
            sleep(1)
            site = BeautifulSoup(navegador.page_source, 'lxml')

            ano_carro = site.find(id='selectAnocarro').find_all('option')

            for l in range(2, len(ano_carro) + 1):
                navegador.find_element('xpath', f'//*[@id="selectAnocarro"]/option[{l}]').click()
                navegador.find_element('xpath', '//*[@id="buttonPesquisarcarro"]').click()
                sleep(1)

                site = BeautifulSoup(navegador.page_source, 'lxml')

                informacoes = site.find('tbody').find_all('td')
                dados = []

                for m in range(len(informacoes)):
                    if m % 2 != 0:
                        dados.append(re.sub('<[^<]+?>', '', str(informacoes[m])))
                print(dados)
                dados.append(todos_dados) #Colocando em todos os dados
                sleep(1)


    print(i)




#res = soup.find('ul', class_='chosen-results')
#print(soup)

