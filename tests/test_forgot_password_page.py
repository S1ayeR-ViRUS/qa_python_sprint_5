from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config
from locators import LocatorsAccountPage, LocatorsForgotPasswordPage, LocatorsLoginPage, LocatorsMainPage
from data import AuthTestData


class TestForgotPasswordPage:
    #Вход в ЛК по ссылке на странице восстановления пароля.
    def test_login_by_click_on_link_in_forgot_password_page(self, driver):
        driver.get(config.URL + config.FORGOT_PASSWORD_PAGE)
        driver.find_element(*LocatorsForgotPasswordPage.LOGIN_LINK).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsLoginPage.TEXT_LOGIN, 'Вход'))
        driver.find_element(*LocatorsLoginPage .LOGIN_EMAIL_INPUT).send_keys(*AuthTestData.AUTH_EMAIL)
        driver.find_element(*LocatorsLoginPage.LOGIN_PASSWORD_INPUT).send_keys(*AuthTestData.AUTH_PASSWORD)
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        driver.find_element(*LocatorsMainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsAccountPage.PROFILE_BUTTON, 'Профиль'))
        assert driver.current_url == config.URL + config.ACCOUNT_PAGE