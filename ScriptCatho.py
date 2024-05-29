from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.catho.com.br/vagas/ti/sao-paulo-sp/"

def buscarDados(url):
    driver = webdriver.Chrome()
    driver.get(url)  
    news = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[3]')

    for element in news:
        try:
          elementChildren = element.find_elements(By.TAG_NAME, "header")
          for elementChild in elementChildren:            
            # Aguardar até que o elemento <a> seja visível
            a_element = WebDriverWait(elementChild, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "a"))
            )
            
            print("---------- VAGA ENCONTRADA --------------")
            print(elementChild.text) 
            print("Link da Vaga: " + a_element.get_attribute('href'))
        except:
          print("")
    
    driver.quit()

buscarDados(url)
