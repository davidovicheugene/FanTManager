from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from book_data import *
from config import rulate_profiles_ids, EC_wait_secs


def get_profile_page_r(driver, username):
    """Redirect to profile page

    Args:
        driver (selenium.webdriver): Webdriver with authenticated user
        username (str): _description_

    Returns:
        driver (selenium.webdriver): webdriver with profile page
    """
    driver.get(f"https://tl.rulate.ru/users/{rulate_profiles_ids[username]}")
    return driver


def get_profile_info_r(driver, user_id):
    """Gets basic profile info of any user

    Args:
        driver (selenium.webdriver): Webdriver
        user_id (int): rulate User ID

    Returns:
        driver (selenium.webdriver): webdriver
        data (dict): basic data of the user
        
    """
    # Redirect to user profile page
    driver.get(f"https://tl.rulate.ru/users/{user_id}")
    # Getting elements and needed info out of them
    username = driver.find_element(By.ID, "change-login_login").text
    role = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/h1/small[1]"))
    ).text.replace('(', '').replace(')', '').replace(' ', ', ')
    try:
        is_online = WebDriverWait(driver, EC_wait_secs).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/h1/small[2]"))
        ).text
        is_online = True
    except:
        is_online = False
    gender = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/dl/dd[2]"))
    ).text
    native_language = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/dl/dd[3]"))
    ).text
    created_at = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/dl/dd[4]"))
    ).text
    last_online = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/dl/dd[5]"))
    ).text
    total_translated = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/dl/dd[6]"))
    ).text
    send_msg_link = WebDriverWait(driver, EC_wait_secs).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/a"))
    ).get_attribute("href")

    data = {
        "username": username,
        "is_online": is_online,
        "role": role,
        "gender": gender,
        "native_language": native_language,
        "created_at": created_at.split('\n')[0],
        "last_online": last_online,
        "total_translated": total_translated,
        "send_msg_link": send_msg_link,
    }

    return driver, data


def create_novel(driver,
                 novel
                 ):
    driver.get("https://tl.rulate.ru/book/0/edit?typ=A")
    # Click on needed section
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, novel.catalog_section))
    ).click()
    # Original language
    if novel.original_lang != NovelSettingsSelectors.OriginalLang.DEFAULT or novel.original_lang != NovelSettingsSelectors.OriginalLang.ENGLISH:
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NovelSettingsSelectors.OriginalLang.SELECT_))
        ).click()
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, novel.original_lang))
        ).click()
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NovelSettingsSelectors.OriginalLang.SELECT_))
        ).click()
    # Original title
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_s_title"))
    ).send_keys(novel.original_title)
    # Translation language
    if novel.original_lang != NovelSettingsSelectors.TranslationLang.DEFAULT or novel.original_lang != NovelSettingsSelectors.TranslationLang.RUSSIAN:
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NovelSettingsSelectors.TranslationLang.SELECT_))
        ).click()
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, novel.translation_lang))
        ).click()
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NovelSettingsSelectors.TranslationLang.SELECT_))
        ).click()
    # Translated title
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_t_title"))
    ).send_keys(novel.translation_title)
    # Author
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_author"))
    ).send_keys(novel.author)
    # novelupdates.com link
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_novelupdates"))
    ).send_keys(novel.novelupdates_link)
    # webnovel.com link
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_webnovel_url"))
    ).send_keys(novel.webnovel_link)
    # Publication year
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_year"))
    ).send_keys(novel.publication_year)
    # Total chapters original has
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_chapters_total"))
    ).send_keys(novel.total_chapters)
    # Alternative title 1
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_a_title_1"))
    ).send_keys(novel.alternative_title_1)
    # Alternative title 2
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_a_title_2"))
    ).send_keys(novel.alternative_title_2)
    # Alternative title 3
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_a_title_3"))
    ).send_keys(novel.alternative_title_3)
    # Download access
    if not novel.b_download_access:
        WebDriverWait(driver, EC_wait_secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#Book_disable_download"))
        ).click()
    # Next btn click
    WebDriverWait(driver, EC_wait_secs).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#general > div:nth-child(14) > div > a"))
    ).click()

    return driver
