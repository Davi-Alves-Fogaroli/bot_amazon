# lIBS
from dotenv import load_dotenv
import json
import os
# EXCEPTIONS
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
# WEBDRIVER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

print("....Start....")

load_dotenv()

# configure and define webDriver
options = Options()
#options.headless = True # <- Hability this opition to run in server

try :
    # define driver and accesse website
    s = Service(os.environ.get("DRIVER_PATCH"))
    driver = webdriver.Chrome(service=s, options=options)
    driver.get("https://www.amazon.com.br/")
    driver.maximize_window()

except SessionNotCreatedException :
    print("Verify you crhomedriver driver version") 

# locate the search bar, input the specific key and search for...
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone" + Keys.ENTER)

# wait page load
#WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "sg-col-inner")))


# find all products cards and some garbage
cards = driver.find_elements(By.CLASS_NAME, "sg-col-inner")
#print("cards_______:",cards)

count = 1
dic= {}
file = open('json/data_iphone.json', 'w', encoding ='utf8') 
list=[]
# take name and price 

for x in cards:
    try :
        # find price
        price_whole = x.find_element(By.CLASS_NAME, "a-price-whole").text
        price_fraction = x.find_element(By.CLASS_NAME, "a-price-fraction").text
        price = "R$"+price_whole+","+price_fraction
        #print(f"{count}_price:", price)

        # find name
        #name = x.find_element(By.XPATH, ".//span[@class='a-size-base a-color-base a-text-normal']").text
        name = WebDriverWait(x, timeout=0.5).until(EC.visibility_of_element_located((By.XPATH, ".//span[@class='a-size-base a-color-base a-text-normal']")))
        name = name.text
        print(name,"\n")

        # temporary storage
        dic[name]= price
        #print("_"*100,dic)

    except NoSuchElementException:
        print(f"{count}_element not found", "\n")
        count+=1
    
    except TimeoutException:
        print(f"{count}_search time out", "\n")
        count+=1
    count+=1
    
# final storage
list.append(dic)
json.dump(list, file, indent=2)    

print("_"*100,dic)
file.close()
