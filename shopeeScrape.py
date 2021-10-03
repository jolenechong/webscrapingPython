from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

url = 'https://shopee.sg/%E3%80%90kiel%E3%80%91Character-Spongebob-Patrick-Enamel-Jacket-Brooch-Pins-i.59416510.7105617847'

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url)
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds so that website loads before finding text
price = driver.find_element_by_class_name('Ybrg9j').text
title = driver.find_element_by_class_name('attM6y').find_element_by_tag_name('span').text

print(title,price)
