

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def deposit_250_to_harry():
    driver = webdriver.Chrome('D:\Desktop\chromedriver_win32.exe/')
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    time.sleep(2)

    driver.maximize_window()
    time.sleep(1)

    costumer_login = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
    costumer_login.click()
    time.sleep(1)

    open_window = driver.find_element(By.CSS_SELECTOR, '#userSelect')
    open_window.click()
    time.sleep(1)

    select_user = driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(3)')
    select_user.click()
    time.sleep(1)

    login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')
    login.click()
    time.sleep(1)

    deposit =driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    deposit.click()
    time.sleep(2)

    deposit = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    deposit.send_keys('250')
    time.sleep(2)

    deposit_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    deposit_button.click()
    time.sleep(2)

    Transaction = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
    Transaction.click()
    time.sleep(2)

    amount = driver.find_element(By.CSS_SELECTOR,'#anchor0 > td:nth-child(2)')
    return amount.text

def add_costumer_as_manager():
    driver = webdriver.Chrome('D:\Desktop\chromedriver_win32.exe/')
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    driver.get(url)
    time.sleep(1)

    driver.maximize_window()
    time.sleep(1)

    manager_login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    manager_login.click()
    time.sleep(1)

    add_costumer = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
    add_costumer.click()
    time.sleep(1)

    first_name = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input')
    first_name.send_keys('Reut')
    time.sleep(1)

    last_name = driver.find_element(By.CSS_SELECTOR , 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
    last_name.send_keys('Provisor')
    time.sleep(1)

    post_code = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
    post_code.send_keys('405611')
    time.sleep(1)

    add = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
    add.click()
    time.sleep(1)

    driver.switch_to.alert.accept()
    time.sleep(1)

    costumers = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
    costumers.click()
    time.sleep(2)

    if 'Reut' in driver.page_source:
        return True
    else:
        return False

def add_new_customer_without_first_name():
    driver = webdriver.Chrome('D:\Desktop\chromedriver_win32.exe/')
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    time.sleep(1)

    driver.maximize_window()
    time.sleep(1)

    manager_login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    manager_login.click()
    time.sleep(2)

    add_costumer = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
    add_costumer.click()
    time.sleep(1)

    last_name = driver.find_element(By.CSS_SELECTOR , 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
    last_name.send_keys('Provisor')
    time.sleep(1)

    post_code = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
    post_code.send_keys('405611')
    time.sleep(1)

    add = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
    add.click()
    time.sleep(1)

    return False

def sanity_test_current_url():
    driver = webdriver.Chrome('D:\Desktop\chromedriver_win32.exe/')
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    driver.maximize_window()
    time.sleep(1)

    return driver.current_url

