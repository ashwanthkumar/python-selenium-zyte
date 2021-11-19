from seleniumwire import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(options=options)
browser.get("https://whatsmyip.com/")
browser.save_screenshot("screenshot-new.png")
browser.close()
browser.quit()