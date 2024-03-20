import os.path

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle

from config import prelogin_rulate_url
from users_data import rulate_data


def set_rand_useragent():
    from fake_useragent import UserAgent
    fk_ua = UserAgent()
    fk_useragent = fk_ua.random
    options = Options()
    options.add_argument(f'user-agent={fk_useragent}')
    return options


def save_session(driver, username):
    # Get all cookies from the current session
    cookies = driver.get_cookies()
    # Dump cookies
    pickle.dump(cookies, open(f'sessions/{username}', "wb"))


def set_cookies(driver, username):
    # Send cookies to driver at for loop
    for cookie in pickle.load(open(f'sessions/{username}', 'rb')):
        driver.add_cookie(cookie)
    return driver


def auth_r(driver, username):
    """Authenticates rulate user (profile)

    Args:
        driver (selenium.webdriver): Selenium driver with not authorized rulate user
        username (str): username of the user you want to authenticate

    Returns:
        driver (selenium.webdriver): webdriver with authenticated profile
    """
    # Pre-login page loading
    driver.get(prelogin_rulate_url)
    # Check if needed session exists else authorize
    if os.path.exists(f'sessions/{username}'):
        set_cookies(driver, username)
    else:
        # Find profile btn
        profile_btn = driver.find_element(By.CLASS_NAME, 'main-header-avatar')
        profile_btn.click()
        # Find login inputs and btn
        login_form = driver.find_element(By.XPATH, '//*[@id="header-login"]/form').find_elements(By.TAG_NAME, 'input')
        login_input = login_form[0]
        pass_input = login_form[1]
        login_btn = login_form[2]
        # Push auth data and log in
        login_input.send_keys(username)
        pass_input.send_keys(rulate_data.get(username))
        login_btn.click()
        save_session(driver, username)
    return driver
