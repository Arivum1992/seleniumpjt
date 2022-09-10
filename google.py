from selenium import webdriver
driver=webdriver.Chrome(executable_path="C://Users//ARIVU//PycharmProjects//SeleniumTraining//Driver//chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Today is our 1st automation class")
driver.find_element_by_name("btnk").click()
print("Test completed successfully")
driver.close()
driver.quit()