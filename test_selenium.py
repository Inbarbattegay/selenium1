from seleniumDemo import *
from selenium import webdriver
import pytest

class TestUI:

        #Deposit 250 NIS as an existing user
    def test_harry_potter_deposit_250_in_the_bank(self):
        actual = deposit_250_to_harry()
        expected = '250'
        assert actual == expected

        #add costumer as manger
    def test_add_costumer_as_manager(self):
        actual = add_costumer_as_manager()
        expected = True
        assert actual == expected

        #add costumer as manager without adding first name (N)
    def test_add_new_customer_without_first_name(self):
        actual = add_new_customer_without_first_name()
        expected = False
        assert actual == expected

        #sanity test open website
    def test_url(self):
        driver = webdriver.Chrome('D:\Desktop\chromedriver_win32.exe/')
        actual = sanity_test_current_url()
        expected = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        assert actual == expected
