from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.minimize_window()
# web1 = driver.get('https://tiket.com')
# web2 = driver.get('https://tokopedia.com')
# web3 = driver.get('https://orangsiber.com')
# web4 = driver.get('https://demoqa.com')
# web5 = driver.get('https://automatetheboringstuff.com')

web = ['https://tiket.com','https://tokopedia.com','https://orangsiber.com','https://demoqa.com','https://automatetheboringstuff.com']

for i in web :
    driver.get(i)
    sleep(2)
    print(i," - ", driver.title)
   
driver.close()