import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"D:\BrowserDriver"

driver = webdriver.Chrome()
driver.get("https://www.techwithtim.net/")
print(driver.title)

# serch = driver.find_element(By.NAME , "s")
# serch.send_keys("test")
# serch.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver , 10 ).until(
#         EC.presence_of_element_located((By.ID , "main"))
#     )
#     print(main.text)
#     articles = main.find_elements(By.TAG_NAME, "article")
#     print("articles" , articles)
#     for article in articles :
#         title= article.find_element( By.CLASS_NAME , "entry-title")
#         summary = article.find_element(By.CLASS_NAME, "entry-summary")
#         print("title",title.text)
#         print("summary",summary.text)
# finally :
#     driver.quit()
#
# time.sleep(5)
# driver.quit()



link = driver.find_element(By.LINK_TEXT , "Python Programming")
link.click()
try:
    element = WebDriverWait(driver , 60).until(
        EC.presence_of_element_located((By.LINK_TEXT , "Beginner Python Tutorials"))
    )
    element.click()
    element2 = WebDriverWait(driver , 60).until(
        EC.presence_of_element_located((By.ID ,"sow-button-19310003"))
    )
    element2.click()
except :
    print("i'm quiting")
    driver.quit()