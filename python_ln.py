import json
import time
from selenium import webdriver
# EXCEPTIONS
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import SessionNotCreatedException
# WEBDRIVER
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

print("....Start....")

# configure and define webDriver
options = Options()
# options.headless = True # <- Hability this opition to run in server
PATH = "C:/Users/Italinea/Desktop/dev/python_pl/driver/chromedriver_101.exe"

try :
    # define driver and accesse website
    driver = webdriver.Chrome(PATH, options=options)
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

# take, name and price 
count=1
for x in cards:
    try :
        price_whole = x.find_element(By.CLASS_NAME, "a-price-whole").text
        price_fraction = x.find_element(By.CLASS_NAME, "a-price-fraction").text
        price = "R$"+price_whole+","+price_fraction 
        print(f"{count}_price:", price)

        name = WebDriverWait(x, timeout=5).until(EC.visibility_of_element_located((By.XPATH, ".//span[@class='a-size-base a-color-base a-text-normal']")))
        name = name.text
        print(name,"\n")

    except NoSuchElementException:
        print(f"{count}_not a product", "\n")
        count+=1
    
    except TimeoutException:
        print(f"{count}check your connection speed, please", "\n")

    count+=1

# # find name
# # find price

# #print("1"*200,"\n",nome)
# #print("-"*50,"/n",preco)
