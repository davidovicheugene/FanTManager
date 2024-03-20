import time

from selenium import webdriver

import config
from auth import *
from site_actions import *

if __name__ == "__main__":
    options = set_rand_useragent()
    driver = webdriver.Chrome(options=options)
    driver = auth_r(driver, config.t_auth_username)
    print("Quiting driver")
    driver.quit()
