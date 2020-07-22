import pytest
import os
import textwrap
import copy

from appium import webdriver
from helpers import ANDROID_BASE_CAPS
from helpers import EXECUTOR


class TestAndroidBasicInteractions():
   
    platformName = 'Android'
    deviceName =   'emulator-5554'
    PACKAGE =     'com.example.vamsi.login'
    MAIN_ACTIVITY = '.MainActivity'

    @pytest.fixture(scope='function')
    def driver(self, request):

        caps = copy.copy(ANDROID_BASE_CAPS)
        caps['appActivity'] = self.MAIN_ACTIVITY

        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=caps
        )

        def fin():
            

            driver.quit()

        request.addfinalizer(fin)

        driver.implicitly_wait(10)
        return driver

    def test_cadastro_usurario(self, driver):
        driver.start_activity(self.PACKAGE, self.MAIN_ACTIVITY)
        botao_registro = driver.find_element_by_id("com.example.vamsi.login:id/tvRegister")
        botao_registro.click() 
        campo_name = driver.find_element_by_id("com.example.vamsi.login:id/etRegName")      
        campo_name.send_keys('Guilherme')
        campo_phone = driver.find_element_by_id("com.example.vamsi.login:id/etRegPhone")      
        campo_phone.send_keys('970448966')
        campo_gmail = driver.find_element_by_id("com.example.vamsi.login:id/etRegGmail")      
        campo_gmail.send_keys('gsantos@gmail.com')
        campo_password = driver.find_element_by_id("com.example.vamsi.login:id/etRegPassword")      
        campo_password.send_keys('123456')
        botao_register = driver.find_element_by_id("com.example.vamsi.login:id/btnRegLogin")      
        botao_register.click()
        botao_login_register = driver.find_element_by_id("com.example.vamsi.login:id/btnGotoLogin")      
        botao_login_register.click()
        campo_gmail_valido = driver.find_element_by_id("com.example.vamsi.login:id/etLogGmail")      
        campo_gmail_valido.send_keys('gsantos@gmail.com')    
        campo_password_valido = driver.find_element_by_id("com.example.vamsi.login:id/etLoginPassword")      
        campo_password_valido.send_keys('123456')
        botao_login = driver.find_element_by_id("com.example.vamsi.login:id/btnLogin")      
        botao_login.click()

    def test_login_invalido(self, driver):
        driver.start_activity(self.PACKAGE, self.MAIN_ACTIVITY)
        botao_registro = driver.find_element_by_id("com.example.vamsi.login:id/tvRegister")
        botao_registro.click() 
        campo_name = driver.find_element_by_id("com.example.vamsi.login:id/etRegName")      
        campo_name.send_keys('Sophia')
        campo_phone = driver.find_element_by_id("com.example.vamsi.login:id/etRegPhone")      
        campo_phone.send_keys('988448966')
        campo_gmail = driver.find_element_by_id("com.example.vamsi.login:id/etRegGmail")      
        campo_gmail.send_keys('ssantos@gmail.com')
        campo_password = driver.find_element_by_id("com.example.vamsi.login:id/etRegPassword")      
        campo_password.send_keys('123456')
        botao_register = driver.find_element_by_id("com.example.vamsi.login:id/btnRegLogin")      
        botao_register.click()
        botao_login_register = driver.find_element_by_id("com.example.vamsi.login:id/btnGotoLogin")      
        botao_login_register.click()
        campo_gmail_valido = driver.find_element_by_id("com.example.vamsi.login:id/etLogGmail")      
        campo_gmail_valido.send_keys('msantos@gmail.com')    
        campo_password_valido = driver.find_element_by_id("com.example.vamsi.login:id/etLoginPassword")      
        campo_password_valido.send_keys('12345678')
        botao_login = driver.find_element_by_id("com.example.vamsi.login:id/btnLogin")      
        botao_login.click()  




    