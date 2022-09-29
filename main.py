# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent

# options
options = webdriver.ChromeOptions()

# change useragent
useragent = UserAgent()

options.add_argument(f"user-agent={useragent.random}")
options.add_argument('--ignore-certificate-errors')
options.set_capability('acceptInsecureCerts', True)

login = 'user91743'
password = '6o1dln'

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@185.212.112.158:7104"
    }
}

driver = webdriver.Chrome(
    executable_path="chrome/chromedriver.exe",
    chrome_options=options,
    seleniumwire_options=proxy_options,

)

try:
    driver.get("https://2ip.ru")
    time.sleep(20)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
