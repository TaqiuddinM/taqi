from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import prayerSelect2 as ps


taqiName = 'Muhammad Taqiuddin Bin Mohamed Zaini'
#ACTUAL
#taqiEmail = 'tqdin1993@gmail.com'
#aqiNumber = '92317261'

#TEST
taqiEmail = 'taqiuddin.mz@gmail.com' #tester
taqiNumber = '98359264' #tester

hajiName = 'Mohamed Rahim Bin Hassan'
#ACTUAL
#hajiEmail = 'hajimohdrahim.232@gmail.com'
#hajiNumber = '656507456'

#TEST
hajiEmail = 'taqiuddin93@outlook.com' #tester
hajiNumber = '65650443' #tester


pageurl = 'https://ourmosques.commonspaces.sg/'
driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')


def selectDaily():
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        selectDaily()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()


    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        selectDaily()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()


def selectEnding():
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
        time.sleep(3)
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


def insertDetailsTaqi():
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)


def insertDetailsHaji():
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)


def location():
    element = WebDriverWait(driver, 5).until(
            ##ACTUAL MUKMININ
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label[@clickable='true']")),
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label[@clickable='true']"))

            ##TESTER HUDA
            # EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label[@clickable='true']")),
            # EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label[@clickable='true']"))

        )


def clickLocation():
    ##ACTUAL MUKMININ
    driver.find_element_by_xpath(
        "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label[@clickable='true']").click()

    ##TESTER HUDA
    # driver.find_element_by_xpath("/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label[@clickable='true']").click()
