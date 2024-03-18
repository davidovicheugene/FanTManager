from selenium import webdriver

from time import sleep

import config
from auth import auth_r
from site_actions import *
from config import *

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver = auth_r(driver, t_auth_username)
    # driver = get_profile_page_r(driver, "Honyaku_Hajime")

    # Novel instance creation
    novel = config.n
    driver = create_novel(driver,
                          novel)
    sleep(100)
    driver.quit()
