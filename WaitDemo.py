from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C://Users//ARIVU//PycharmProjects//SeleniumTraining//Driver//chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Automation class")
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.NAME,"btnk")))
#driver.find_element_by_name("btnk").click()
print("Test completed successfully")
driver.close()
driver.quit()