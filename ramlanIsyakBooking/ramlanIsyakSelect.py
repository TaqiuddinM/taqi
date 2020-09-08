from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import re
import datetime


ramlanName = 'Ramlan Bin Ishak'
#ACTUAL
ramlanEmail = 'faceoff67@gmail.com'
ramlanNumber = '96451167'

#TEST
#ramlanEmail = 'taqi12303@outlook.com' #tester
#ramlanNumber = '97814689' #tester


#ACTUAL Mukminin
masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label"

#TEST HUDA
#masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label"

pageurl = 'https://ourmosques.commonspaces.sg/'


def ramlanSubuh():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifRamlanSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

        dateValue = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').text
        if (dateValue == "Invalid Date"):
            driver.close()
            print("ramlanSubuh INVALID DATE ERROR")
            ifRamlanSubuhError()
        else:
            print(dateValue)

    except Exception:
        print("Can't locate date")
        driver.close()
        ifRamlanSubuhError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_1]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifRamlanSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifRamlanSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("RamlanSUBUH Retrieving available capacity ERROR")
            driver.close()
            ifRamlanSubuhError()

        else:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, masjidXPATH)),
                driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

            )


    except Exception:
        print("RamlanSUBUH not clickable uhh MASJID")
        driver.close()
        ifRamlanSubuhError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(ramlanName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(ramlanEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(ramlanEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(ramlanNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    result = driver.current_url
    x = re.search("booking-daily-success", result)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(current_time)
    if x:
        print('ramlanSubuh Booked!')
    else:
        print('ramlanSubuh TOO LATE')
    driver.close()


def ramlanIsyak():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't locate daily")
        driver.close()
        ifRamlanIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

        dateValue = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').text
        if (dateValue == "Invalid Date"):
            driver.close()
            print("ramlanIsyak INVALID DATE ERROR")
            ifRamlanIsyakError()
        else:
            print(dateValue)

    except Exception:
        print("Can't locate date")
        driver.close()
        ifRamlanIsyakError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_5]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifRamlanIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_5]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifRamlanIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("RamlanIsyak Retrieving available capacity... error")
            driver.close()
            ifRamlanIsyakError()

        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )

    except Exception:
        print("RamlanISYAK not clickable uhh MASJID")
        driver.close()
        ifRamlanIsyakError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(ramlanName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(ramlanEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(ramlanEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(ramlanNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("Ramlan clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    result = driver.current_url
    x = re.search("booking-daily-success", result)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(current_time)
    if x:
        print('ramlanIsyak Booked!')
    else:
        print('ramlanIsyak TOO LATE')
    driver.close()


def ifRamlanSubuhError():
    ramlanSubuh()
    ramlanIsyak()
    sys.exit()


def ifRamlanIsyakError():
    ramlanIsyak()
    sys.exit()

