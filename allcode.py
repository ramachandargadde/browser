from selenium import webdriver
from selenium.webdriver.common.by import By
import multiprocessing
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import multiprocessing
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
import time
baseurl="https://10.104.119.76"
baseurl1="https://10.104.119.201"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
driver.get(baseurl)
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"label_username").send_keys("root")
driver.find_element(By.ID,"label_password").send_keys("Public123")
driver.find_element(By.ID,"loginPage_LoginButton_label").click()
driver.execute_script("window.open('" + baseurl1 + "');")
driver.quit(baseurl)
#driver.close(baseurl)
#time.sleep(10)
#driver.close(baseurl)
#driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND +
#ActionChains(webdriver).send_keys(Keys.CONTROL, "t").perform()
driver.execute_script("window.open('" + baseurl1 + "');")

#driver.find_element(By.CSS_SELECTOR,'toggleIcon icon-cisco-menu').click()

#driver.execute_script("window.open('" + baseurl1 + "');")

#driver.find_element(By.ID,"searchResultsDialog").send_keys("Public123")
wait_time = 10 # a very long wait time
element = WebDriverWait(driver, wait_time).\
    until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add')))
#element.click()
#driver.find_element_by_class_name("dijitReset dijitInline dijitButtonNode").click()

driver.find_element(By.XPATH,"//table[@id='xwt_widget_form_TextButton_1_label']").click()
#driver.find_element(By.CLASS,"dijitReset dijitInline dijitButtonText").click()
print('chandu')




def chromedriver_function(url):
    driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
    driver.get(url)
    driver.find_element(By.ID,"details-button").click()
    driver.find_element(By.ID,"proceed-link").click()
    driver.find_element(By.ID,"label_username").send_keys("root")
    driver.find_element(By.ID,"label_password").send_keys("Public123")
    driver.find_element(By.ID,"loginPage_LoginButton_label").click()
    return driver.page_source


chromedriver_function("https://10.104.119.75")
#chromedriver_function("https//:10.104.119.76")

#driver.get.Windowhandles


time.sleep(5)
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'details-button')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

baseurl="https://10.197.72.84"
baseurl1="https://10.104.119.201"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
driver.get(baseurl)
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"label_username").send_keys("root")
driver.find_element(By.ID,"label_password").send_keys("roZes123")
driver.find_element(By.ID,"loginPage_LoginButton_label").click()
time.sleep(10)
delay=3
dnacurl=baseurl+"/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en&#pageId=dnac_integration_page_id"
driver.execute_script("window.open('" +dnacurl + "');")
time.sleep(10)
#delay=3
#dnacurl=baseurl+"/webacs/loginAction.do?action=login&product=wcs&selectedCategory=en&#pageId=dnac_integration_page_id"
#driver.execute_script("window.open('" +dnacurl + "');")

#time.sleep(1000000)
#baseurl="https://10.197.72.116"
#baseurl2="https://10.197.72.115"