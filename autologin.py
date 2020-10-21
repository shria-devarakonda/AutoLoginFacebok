from selenium import webdriver
import argparse as ap
import time

parser = ap.ArgumentParser(description='Enter your email ID and Password')
parser.add_argument("email")
parser.add_argument("password")
args = parser.parse_args()

path = r"C:\Users\shria\Desktop\Selenium\geckodriver\geckodriver.exe"
#edit above path according to your geckodriver.exe path

driver = webdriver.Firefox(executable_path=path)
driver.maximize_window()

driver.get("https://www.facebook.com/")

emailID = driver.find_element_by_css_selector('#email')
emailID.clear()
emailID.send_keys(args.email)

passw = driver.find_element_by_css_selector('#pass')
passw.clear()
passw.send_keys(args.password)

loginBtn=driver.find_element_by_css_selector('#u_0_b')
loginBtn.click()

time.sleep(15)
driver.close()
#browser will close after 15 seconds
