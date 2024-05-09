import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config
from data import AuthTestData
from locators import LocatorsAccountPage, LocatorsLoginPage, LocatorsMainPage


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(config.URL)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get(config.URL + config.LOGIN_PAGE)
    driver.find_element(*LocatorsLoginPage.LOGIN_EMAIL_INPUT).send_keys(*AuthTestData.AUTH_EMAIL)
    driver.find_element(*LocatorsLoginPage.LOGIN_PASSWORD_INPUT).send_keys(*AuthTestData.AUTH_PASSWORD)
    driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
    driver.find_element(*LocatorsMainPage.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsAccountPage.PROFILE_BUTTON, 'Профиль'))