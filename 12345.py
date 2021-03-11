from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from servers import UI_servers
# from servers import Pi_pages
import string
# page=Pi_pages()
cd=UI_servers()
# print(cd.__init__.__code__.co_nlocals)
Software_update_page="webacs/loginAction.do?action=login&product=wcs&selectedCategory=en#pageId=Software_Update_pageId&forceLoad=true"
passwd="Public123"
# passwd="roZes123"
driver = webdriver.Chrome(executable_path="C:\\Users\\ramacgad\\Desktop\\software updates\\3.7\\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe")
driver.get(cd.url75)
# driver.execute_script("window.open('" +cd.url76+ "');")
# driver.execute_script("window.open('" +cd.url78+ "');")
# driver.execute_script("window.open('" +cd.url79+ "');")
driver.execute_script("window.open('" +cd.url80+ "');")
driver.execute_script("window.open('" +cd.url209+ "');")
driver.execute_script("window.open('" +cd.url221+ "');")
driver.execute_script("window.open('" +cd.url198+ "');")
allTabs=driver.window_handles
print(allTabs)
for tab in allTabs:
    try:
        driver.switch_to.window(tab)
        driver.find_element(By.ID,"details-button").click()
        driver.find_element(By.ID,"proceed-link").click()
        driver.find_element(By.ID,"label_username").send_keys("root")
        driver.find_element(By.ID,"label_password").send_keys(passwd)
        driver.find_element(By.ID,"loginPage_LoginButton_label").click()
        time.sleep(10)
        url=str(driver.current_url)
        ip=''
        for char1 in url:
            if char1 != 'w':
                ip=ip+char1
            else:
                break
        print(ip)
        # driver.get(ip+Software_update_page)
        # print("login successful")
        # time.sleep(10)
        # driver.find_element_by_link_text("upload").click()
        # print('upload click done')
        # time.sleep(5)
        # # driver.find_element_by_id('browseUploadDialog').click()
        # # driver.find_element('Browse').click()
        # # driver.find_element_by_xpath("//*[@id='browseUploadDialog']").click()
        # # driver.find_element_by_id('browseUploadDialog').send_keys("C:\\PI_upload_files\\PI_3_8_1_DNAC_UBF-1.0.13.ubf")
        # driver.find_element_by_id('browseUploadDialog').click().send_keys('C:\\PI_upload_files\\PI_3_8_1_DNAC_UBF-1.0.13.ubf')
        # print('browse done')

    except():
        print("login failed")
        continue