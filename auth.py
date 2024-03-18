from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from config import prelogin_rulate_url
from users_data import rulate_data


def auth_r(driver, username):
    """Authenticates rulate user (profile)

    Args:
        driver (selenium.webdriver): Selenium driver with not authorized rulate user
        username (str): username of the user you want to authenticate

    Returns:
        driver (selenium.webdriver): webdriver with authenticated profile
    """
    driver.get(prelogin_rulate_url)
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

    return driver