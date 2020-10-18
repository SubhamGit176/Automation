from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from pathlib import Path

src1 = 'https://www.flipkart.com/oppo-reno2-f-sky-white-128-gb/p/itm8413e7eb0b195?pid=MOBFH274NFFY7AZW&lid=LSTMOBFH274NFFY7AZW02MDPK&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=SEARCH&iid=2afcb5eb-2624-4afc-92d4-470935499169.MOBFH274NFFY7AZW.SEARCH&ppt=sp&ppn=sp&ssid=36m05ll1pc0000001602483538350&qH=5d94a2e0ffe57af3'
src2 = 'https://www.amazon.in/Reno2-Storage-Additional-Exchange-Offers/dp/B07XBYMDTG/ref=sr_1_4?dchild=1&keywords=oppo+reno2&qid=1602483573&sr=8-4'



wait_imp = 10

wd = webdriver.Chrome("/home/subham/chromedriver")

print('Starting automation')
print('Connecting to flipkart....')
wd.get(src1)

wd.implicitly_wait(wait_imp)

p_name = wd.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
price = wd.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')

f_product = p_name.text
f_price = price.text

print('Info retrieved from flipkart..')
time.sleep(2)

print('Connecting to amazon....')
wd.get(src2)

wd.implicitly_wait(wait_imp)

p_name = wd.find_element_by_xpath('//*[@id="productTitle"]')
price = wd.find_element_by_xpath('//*[@id="priceblock_ourprice"]')

a_product = p_name.text
a_price = price.text

print('Info retrieved from amazon..')
time.sleep(2)

print(f'Price of {f_product} from different sources are as follows:')
print(f'Flipkart: {f_price}')
print(f'Amazon: {a_price}')



