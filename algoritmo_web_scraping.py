from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re

#78
contador = [8-2, 153-2, 2-2]
print(contador)

navegador = webdriver.Edge()
navegador.set_window_size(800, 600)

navegador.get('https://veiculos.fipe.org.br/')

navegador.find_element('xpath', '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a').click()

sleep(2)

navegador.find_element('xpath', '//*[@id="selectTabelaReferenciacarro"]').click()

sleep(2)

site = BeautifulSoup(navegador.page_source, 'lxml')

anos = site.find(id='selectTabelaReferenciacarro').find_all('option')
marcas = site.find(id='selectMarcacarro').find_all('option')

with open('Base dados.txt', 'a') as bd:
    for i in range(1, len(anos) + 1):
        navegador.find_element('xpath', f'//*[@id="selectTabelaReferenciacarro"]/option[{i}]').click()
        sleep(1)

        for j in range(2 + contador[0], len(marcas) + 1):
            navegador.find_element('xpath', f'//*[@id="selectMarcacarro"]/option[{j}]').click()
            sleep(1)
            site = BeautifulSoup(navegador.page_source, 'lxml')

            ano_modelo = site.find(id='selectAnoModelocarro').find_all('option')

            for k in range(2 + contador[1], len(ano_modelo) + 1):
                navegador.find_element('xpath', f'//*[@id="selectMarcacarro"]/option[{j}]').click()
                sleep(1)

                navegador.find_element('xpath', f'//*[@id="selectAnoModelocarro"]/option[{k}]').click()
                sleep(1)
                site = BeautifulSoup(navegador.page_source, 'lxml')

                ano_carro = site.find(id='selectAnocarro').find_all('option')

                for l in range(2 + contador[2], len(ano_carro) + 1):
                    navegador.find_element('xpath', f'//*[@id="selectAnocarro"]/option[{l}]').click()
                    navegador.find_element('xpath', '//*[@id="buttonPesquisarcarro"]').click()
                    sleep(1)

                    site = BeautifulSoup(navegador.page_source, 'lxml')

                    informacoes = site.find('tbody').find_all('td')
                    dados = []

                    txt = ''
                    for m in range(len(informacoes)):
                        if m % 2 != 0:
                            dados.append(re.sub('<[^<]+?>', '', str(informacoes[m])))
                            txt += re.sub('<[^<]+?>', '', str(informacoes[m])) + ','
                    txt += '\n'
                    bd.write(txt)
                    print(dados)
                    sleep(1)

                    with open('posicoes.txt', 'w') as indexs:
                        indexs.write(f'i:{i}, j:{j}, k:{k}, l:{l}')
                        indexs.close()

                    if l == len(ano_carro):
                        navegador.find_element('xpath', '//*[@id="buttonLimparPesquisarcarro"]/a').click()

            contador[1] = 0
            contador[2] = 0
        contador[0] = 0
    bd.close()


# res = soup.find('ul', class_='chosen-results')
# print(soup)
