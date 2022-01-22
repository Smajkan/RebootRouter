from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import netifaces
 
def getGateway():
    gws = netifaces.gateways()
    gateway = "http://" + str(gws['default'][netifaces.AF_INET][0])
    return gateway

def restartRouter():
    
    driver = webdriver.Chrome('./chromedriver')
    driver.get(getGateway())
    #Frm_Username
    username = driver.find_element(By.NAME,'Frm_Username')
    username.clear()
    username.send_keys("user")
    #Frm_Password
    passwrd = driver.find_element(By.NAME,"Frm_Password")
    passwrd.clear()
    passwrd.send_keys("user")
    #passwrd.send_keys(Keys.RETURN)
    
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"LoginId\"]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mmManagDiag\"]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mmManagDevice\"]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Btn_restart\"]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"confirmOK\"]"))).click()
    driver.quit()
