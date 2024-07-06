from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.implicitly_wait(7)

driver.maximize_window()

driver.get('http://demoqa.com/alerts')

# driver.find_element(By.ID,'alertButton').click()

def alert():
    driver.find_element(By.ID,'alertButton').click()
    try :
        WebDriverWait(driver,4).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("alert muncul sebelum 4 detik")

    except TimeoutException :
        print("alert tidak muncul setelah di tunggu 4 detik")

def alert_5s():
    driver.find_element(By.ID,'timerAlertButton').click()
    try :
        WebDriverWait(driver,6).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("alert di set muncul setelah 5 detik")
    
    except TimeoutException :
        print("alert tidak muncul")

def alert_ok() :
    driver.find_element(By.ID,'confirmButton').click()
    try :
        WebDriverWait(driver,3).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print("You selected Ok")

    except TimeoutException :
        print("tidak ada yang di pencet")

def alert_cancel() :
    driver.find_element(By.ID,'confirmButton').click()
    try :
        WebDriverWait(driver,3).until(EC.alert_is_present())
        driver.switch_to.alert.dismiss()
        print("You selected Cancel")

    except TimeoutException :
        print("tidak ada yang di pencet")

def alert_prompt_box() :
    try :
        driver.find_element(By.ID,'promtButton').click()
        # WebDriverWait(driver,5).until(EC.alert_is_present())
        # driver.switch_to.alert.accept()
        coba = driver.switch_to.alert
        coba.send_keys("ini isi dari text book alert")
        teks = coba.text
        print(teks)
        coba.accept()
        # driver._switch_to.alert.send_keys(coba)
        # coba = driver.switch_to.alert

    except TimeoutException :
        print("tidak ada yang di pencet")

alert()
alert_5s()
alert_ok()
alert_cancel()
alert_prompt_box()

driver.quit()
