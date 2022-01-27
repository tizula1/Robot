import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pesquisa = input("Digite oque você deseja pesquisar:\n")

driver = webdriver.Chrome('/Users/tizula/Desktop/Robos/assets/chromedriver')
driver.get("https://www.google.com")

campo = driver.find_element_by_xpath("//input[@aria-label = 'Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

result = driver.find_element_by_xpath("//div[@id='result-stats']")
print(result.text)
result = re.sub('[0-9]', '', result)
print(result)
'''number_results = int(result.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
max_pages = number_results/10
print("Número de páginas: %s" % (max_pages))'''