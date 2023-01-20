from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import *
import time

options = Options()
options.add_argument("--lang=en")

# Create the drive and connect the website
driver = webdriver.Chrome(options= options)
driver.get('https://www.google.com/maps/@52.2303201,20.9905102,14z')
# give some time to connect the website
time.sleep(2)
# To approve the website cookies notification (for the first time entry) - it only be used in case of necessity
try:
    cookies = driver.find_element(By.CLASS_NAME, 'lssxud')
    cookies.click()
except:
    print('No cookies are preseented. Skipping...')


# Define function to enter the desired search place
def search(place_name):
    place = driver.find_element(By.ID, 'searchboxinput')
    place.send_keys(place_name)
    submit = driver.find_element(By.ID, 'searchbox-searchbutton')
    submit.click()

    driver.implicitly_wait(5)

    # side_list = driver.find_element(By.CLASS_NAME, 'G0bp3e')
    # print('list of side elements : ', side_list.text)

    side_element = driver.find_elements(By.CSS_SELECTOR, 'a[jsan="7.hfpxzc,0.aria-label,8.href,0.jsaction,0.jslog"]')
    side_element[0].click()

    time.sleep(2)

    location_name = driver.find_element(By.CSS_SELECTOR, 'h1[jsan="7.DUwDvf,7.fontHeadlineLarge"]')
    print('location_name : ', location_name.text)

    time.sleep(2)

    location = driver.find_element(By.CSS_SELECTOR, 'div[jsan="7.Io6YTe,7.fontBodyMedium"]')
    print('location : ', location.text)

    time.sleep(2)

    score = driver.find_element(By.CSS_SELECTOR, 'div[jsan="7.fontDisplayLarge"]')
    print('score : ', score.text)

    time.sleep(3)

    # More
    try:
        # more_comments = driver.find_element(By.CSS_SELECTOR, 'span[jsan="7.wNNZR,7.fontTitleSmall"]')
        more_comments = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[44]/div/button/span/span[2]')
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(more_comments).click(more_comments).perform()
        print("found!")
    except:
        print("skipping...")

    time.sleep(2)

    # 'Wiency'
    try:
        more = driver.find_element(By.CSS_SELECTOR,
                                   'button[jsan="7.w8nwRe,7.kyuRq,0.aria-controls,0.data-review-id,0.jslog,0.aria-label,0.aria-expanded,22.jsaction"]')
        more.click()
    except:
        print('skipping..')

    review = driver.find_elements(By.CLASS_NAME, 'wiI7pd')
    print(len(review))
    for i in range(len(review)):
        print('review : ', review[i].text)
        print()


search('wc in istanbul')

print("finished scraping!")
time.sleep(500)