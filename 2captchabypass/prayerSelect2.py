from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import stopRunning2 as stp

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
fifteenTime = "00:12:00"

taqiName = 'Muhammad Taqiuddin Bin Mohamed Zaini'
#ACTUAL
taqiEmail = 'tqdin1993@gmail.com'
taqiNumber = '92317261'

#TEST
#taqiEmail = 'taqiuddin.mz@gmail.com' #tester
#taqiNumber = '98359264' #tester

hajiName = 'Mohamed Rahim Bin Hassan'
#ACTUAL
hajiEmail = 'hajimohdrahim.232@gmail.com'
hajiNumber = '65657456'

#TEST
#hajiEmail = 'taqiuddin93@outlook.com' #tester
#hajiNumber = '65650443' #tester


#ACTUAL Mukminin
masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label"

#TEST HUDA
#masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label"

pageurl = 'https://ourmosques.commonspaces.sg/'


def taqiSubuh():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        iftaqiSubuhError()


    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        iftaqiSubuhError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_1]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        iftaqiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        iftaqiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("taqiSUBUH Retrieving available capacity... error")
            driver.quit()
            iftaqiSubuhError()

        else:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, masjidXPATH)),
                driver.find_element_by_xpath(masjidXPATH).is_enabled() == True
            )

    except Exception:
        print("Subuh not clickable uhh MASJID")
        driver.quit()
        iftaqiSubuhError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)

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
        time.sleep(2)
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
    driver.quit()
    print('taqiSubuh Booked!')

def hajiSubuh():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        ifhajiiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        ifhajiiSubuhError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_1]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        ifhajiiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        ifhajiiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("HAJI SUBUH Retrieving available capacity... error")
            driver.quit()
            ifhajiiSubuhError()

        else:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, masjidXPATH)),
                driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

            )


    except Exception:
        print("HAJI SUBUH not clickable uhh MASJID")
        driver.quit()
        ifhajiiSubuhError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

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
        time.sleep(2)
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
    driver.quit()
    print('hajiSubuh Booked!')


def taqiIsyak():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        iftaqiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        iftaqiIsyakError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_5]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        iftaqiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_5]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        iftaqiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("taqiISYAK Retrieving available capacity... error")
            driver.quit()
            iftaqiIsyakError()

        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True
        )

    except Exception:
        print("TAQI ISYAK not clickable uhh MASJID")
        driver.quit()
        iftaqiIsyakError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)

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
        time.sleep(2)
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
    driver.quit()
    print('taqiIsyak Booked!')


def hajiIsyak():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        ifhajiIsyakError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_5]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_5]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiIsyak Retrieving available capacity... error")
            driver.quit()
            ifhajiIsyakError()

        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI ISYAK not clickable uhh MASJID")
        driver.quit()
        ifhajiIsyakError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

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
        time.sleep(2)
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
    driver.quit()
    print('hajiIsyak Booked!')


def hajiMaghrib():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        ifhajiMaghribError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_4]'))

        )

    except Exception:
        print("Can't located Maghrib")
        driver.quit()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_4]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiMaghrib Retrieving available capacity... error")
            driver.quit()
            ifhajiMaghribError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI MAGHRIB not clickable uhh MASJID")
        driver.quit()
        ifhajiMaghribError()

    else:
        time.sleep(2)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

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

    time.sleep(5)
    driver.quit()
    print('hajiMaghrib Booked!')


def hajiAsar():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        ifhajiAsarError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_3]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_3]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiASAR Retrieving available capacity... error")
            driver.quit()
            ifhajiAsarError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI ASAR not clickable uhh MASJID")
        driver.quit()
        ifhajiAsarError()

    else:
        time.sleep(1)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

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

    time.sleep(5)
    driver.quit()
    print('hajiAsar Booked!')


def hajiZohor():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        ifthajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        ifthajiZohorError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_2]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        ifthajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_2]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        ifthajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiZOHOR Retrieving available capacity... error")
            driver.quit()
            ifthajiZohorError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI ZOHOR not clickable uhh MASJID")
        driver.quit()
        ifthajiZohorError()

    else:
        time.sleep(1)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

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

    time.sleep(5)
    driver.quit()
    print('hajiZohor Booked!')

def taqiMaghrib():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        iftaqiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        iftaqiMaghribError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_4]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        iftaqiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_4]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        iftaqiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("taqiMaghrib Retrieving available capacity... error")
            driver.quit()
            iftaqiMaghribError()
        else:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, masjidXPATH)),
                driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

            )


    except Exception:
        print("TAQI MAGHRIB not clickable uhh MASJID")
        driver.quit()
        iftaqiMaghribError()

    else:
        time.sleep(1)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)

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

    time.sleep(5)
    driver.quit()
    print('taqiMaghrib Booked!')


def taqiAsar():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        iftaqiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        iftaqiAsarError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_3]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        iftaqiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_3]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        iftaqiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("taqiASAR Retrieving available capacity... error")
            driver.quit()
            iftaqiAsarError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("TAQI asar not clickable uhh MASJID")
        driver.quit()
        taqiAsar()

    else:
        time.sleep(2)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)

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

    time.sleep(5)
    driver.quit()
    print('taqiAsar Booked!')


def taqiZohor():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.quit()
        iftaqiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.quit()
        iftaqiZohorError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_2]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.quit()
        iftaqiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_2]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.quit()
        iftaqiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("taqiZohor Retrieving available capacity... error")
            driver.quit()
            iftaqiZohorError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("TAQI zohor not clickable uhh MASJID")
        driver.quit()
        iftaqiZohorError()

    else:
        time.sleep(2)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(taqiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(taqiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(taqiNumber)

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

    time.sleep(5)
    driver.quit()
    print('taqiZohor Booked!')


def iftaqiSubuhError():
    taqiSubuh()
    hajiSubuh()
    taqiIsyak()
    hajiIsyak()
    taqiMaghrib()
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def ifhajiiSubuhError():
    hajiSubuh()
    taqiIsyak()
    hajiIsyak()
    taqiMaghrib()
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def iftaqiIsyakError():
    taqiIsyak()
    hajiIsyak()
    taqiMaghrib()
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def ifhajiIsyakError():
    hajiIsyak()
    taqiMaghrib()
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def iftaqiMaghribError():
    taqiMaghrib()
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def ifhajiMaghribError():
    hajiMaghrib()
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def iftaqiAsarError():
    taqiAsar()
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def ifhajiAsarError():
    hajiAsar()
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def iftaqiZohorError():
    taqiZohor()
    hajiZohor()
    stp.stopRec()


def ifthajiZohorError():
    hajiZohor()
    stp.stopRec()

