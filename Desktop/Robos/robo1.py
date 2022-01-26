from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

print("Iniciando nosso robo...\n")

workbook = pd.read_excel('dominios.xlsx')
lista = workbook['dominio.com.br'].tolist()

arq = open("resultados.txt","w")

driver = webdriver.Chrome('/Users/tizula/Desktop/Robos/assets/chromedriver')
driver.get("http://registro.br/")


dominios = lista

for dominio in dominios :
    pesquisa = driver.find_element(By.ID,"is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_element(By.TAG_NAME, "strong")

    texto = "Domínio %s %s" %(resultados[4])
    arq.write(texto)
arq.close()
driver.close()
