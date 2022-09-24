"""
#Need help link
driver.find_element(By.XPATH,"//span[@class = 'a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID,'auth-fpp-link-bottom')

#Other issues with Sign-In link
driver.find_element(By.ID,'ap-other-signin-issues-link')

#Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')

#Conditions of use link
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//child::a[1]")

#*Privacy Notice link
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//child::a[2]")

"""


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')
driver.find_element(By.ID,'nav-orders').click()

expected_resul = "Sign in"
actual_result = driver.find_element(By.XPATH,"//*[contains(text(),'Sign in')]").text
assert expected_resul == actual_result, f'Error! Expected {expected_resul} , but got {actual_result}.'
print("Test case passed")
driver.quit()