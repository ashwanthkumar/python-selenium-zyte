from seleniumwire import webdriver
import json

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(options=options)
with open("fetch.log", "a") as myfile:
  for number in range(100):
    browser.get("https://httpbin.org/ip")
    pre = browser.find_element_by_tag_name("pre").text
    myfile.write(pre + "\n")

browser.close()
browser.quit()