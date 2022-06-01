# lIBS
# from dotenv import load_dotenv
import json
# import os
# WEBDRIVER
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

print("....Start....")

# load_dotenv()

# configure and define webDriver
options = Options()
#options.headless = True # <- Hability this opition to run in server

try :
    # define driver and accesse website
    s = Service("driver\chromedriver_101.exe")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get("https://www.amazon.com.br/")
    driver.maximize_window()

except SessionNotCreatedException :
    print("Verify you crhomedriver driver version") 

# locate the search bar, input the specific key and search for...
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone" + Keys.ENTER)

# find all products cards and some garbage
card = driver.find_elements(By.CSS_SELECTOR, "div[data-asin]")

count = 1
dic= {}
file = open('json/data_iphone.json', 'w', encoding ='utf8') 
list=[]

for x,y in enumerate(card):
   
    list_text1 = y.text
    list_text1_split = list_text1.split("\n")
    print("--"*30,"\n",list_text1.split("\n"))
    
    if len(list_text1_split) < 4 :
        continue
    
    list2 = ["Oferta","Patrocinado", "PESQUISAS RELACIONADAS", "PRECISA DE AJUDA?", "Nenhuma oferta em destaque disponível"]

    list_boll=[x in y for x in list2 for y in list_text1_split]
    
    if any(list_boll):
        continue

    indice_name = 0
    indice_price = 2
    
    if list_text1_split[0] == "Patrocinados": 
        indice_price += 1
        indice_name += 1
    
    if "Economize" in list_text1_split[2] : indice_price += 1
    
    # take name and price
    name = list_text1_split[indice_name]
    price = list_text1_split[indice_price]
    
    # temporary storage
    dic[name]= price
    
# final storage
list.append(dic)
json.dump(list, file, indent=2)    

print("_"*100,dic)
file.close()
