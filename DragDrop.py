from selenium import webdriver
# for drag and drop function
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source = driver.find_element_by_xpath('//*[@id="box3"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
source1 = driver.find_element_by_xpath('//*[@id="box1"]')
destination1 = driver.find_element_by_xpath('//*[@id="box101"]')
actions1 = ActionChains(driver)
actions.drag_and_drop(source1, destination1).perform()
