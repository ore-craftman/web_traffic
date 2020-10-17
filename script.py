from selenium import webdriver
import time


x = 1
while x<500:
    #Get Google
    web = webdriver.Chrome()
    web.get('https://www.google.com')
    time.sleep(2)

    #Search for term
    search_bar = web.find_element_by_css_selector('input[name=q]')
    search_bar.send_keys('royalng .com')
    search_bar.submit()
    time.sleep(2)

    #Get Website from search Result by xpath
    royal_ng = web.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')
    royal_ng.click()
    time.sleep(15)

    # Cancel Push Notification and Popup on the site
    push_notification = web.find_element_by_xpath('//*[@id="onesignal-slidedown-cancel-button"]')
    push_notification.click()
    time.sleep(2)

    pop_up = web.find_element_by_xpath('//*[@id="sgpb-popup-dialog-main-div-wrapper"]/div/img')
    pop_up.click()
    time.sleep(2)

    x += 1

time.sleep(86400)

