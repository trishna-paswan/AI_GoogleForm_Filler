# form_filler.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_google_form(data, form_url):
    driver = webdriver.Chrome()
    driver.get(form_url)
    time.sleep(2)

    # Replace with actual XPaths from your Google Form
    xpaths = {
        "Name": '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
        "Email": '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        "Phone": '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        "DOB": '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
        "Address": '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
        "Submit": '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    }

    for key in ["Name", "Email", "Phone", "DOB", "Address"]:
        if data.get(key):
            input_box = driver.find_element(By.XPATH, xpaths[key])
            input_box.send_keys(data[key])
            time.sleep(1)

    submit_btn = driver.find_element(By.XPATH, xpaths["Submit"])
    submit_btn.click()
    time.sleep(2)
    driver.quit()

'''
✅ How to Correctly Get the XPath:

Please do the following exact steps:

Open your Google Form.

Right-click inside the Full Name input box (not on the label).

Click Inspect.

You will be taken to the corresponding <input type="text"> in the Elements tab.

Right-click that <input> element → Choose Copy > Copy XPath.
'''
