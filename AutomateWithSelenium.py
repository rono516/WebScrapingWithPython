from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://studentportal.helb.co.ke/auth/signin")
emailField = driver.find_element_by_xpath('//*[@id="form-email_add"]')
emailField.send_keys('ronocollins2000@gmail.com')
passwordField = driver.find_element_by_xpath('//*[@id="form-password"]')
passwordField.send_keys('37842681')
LoginButton = driver.find_element_by_xpath('//*[@id="form-login"]/button')
LoginButton.click()
# from selenium import webdriver
# import chromedriver_autoinstaller
#
# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
# # and if it doesn't exist, download it automatically,
# # then add chromedriver to path
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
