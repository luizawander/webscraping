from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://g1.globo.com/"
def buscarDados(url):
  driver = webdriver.Chrome()
  driver.get(url)  
  news = driver.find_element(By.XPATH, '//*[@id="feed-placeholder"]/div/div/div[2]/div/div/div')
  driver.quit()
  return news

teste = buscarDados(url)

print(teste)

