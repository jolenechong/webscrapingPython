'''for dynamically loaded/javascript webpages - lazada'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

url = 'https://www.lazada.sg/products/apple-macbook-air-13-inch-apple-m1-chip-with-8-core-cpu-and-7-core-gpu-256gb-i1344610364-s5655346807.html'

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.get(url)
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds
price = driver.find_element_by_id('module_product_price_1').find_element_by_tag_name('span').text

print(price)

'''scrape more data in lazada'''

# url = 'https://www.lazada.sg/catalog/?q=Apple+MacBook+Air+13-inch&_keyori=ss&from=input&spm=a2o42.pdp_revamp.search.go.7c2c2a99f33Vh6'
#
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
#
# driver.get(url)
# driver.implicitly_wait(10) # gives an implicit wait for 10 seconds
#
# for i in range(10):
#     title = driver.find_elements_by_class_name('_8JShU')[i].find_element_by_tag_name('a').text
#     price = driver.find_elements_by_class_name('Q78Jz')[i].text
#     print(title,"\n",price)
