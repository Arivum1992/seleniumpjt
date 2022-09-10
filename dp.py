from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C://Users//ARIVU//PycharmProjects//SeleniumTraining//Driver//chromedriver.exe")
driver.get("https://dineshpitchuka.teachable.com/")
driver.find_element_by_partial_link_text("Login").click()
driver.find_element_by_xpath("//*[@id='email']") .send_keys("arivazhagan.m96@gmail.com")
driver.find_element_by_id("password").send_keys("arivu9626")
driver.find_element_by_name("commit").click()
driver.find_element_by_class_name("col-xs-12.course-listing-enrolled") .click()
print("Test Completed Successfully")
time.sleep(10)
driver.close()
driver.quit()