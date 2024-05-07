import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config
from locators import LocatorsAccountPage, LocatorsLoginPage, LocatorsMainPage
from data import AuthTestData


class TestMainPage:
    # Вход в ЛК по кнопкам "Войти в аккаунт" и "Личный кабинет" на главной странице.
    @pytest.mark.parametrize('button', [LocatorsMainPage.ACCOUNT_BUTTON, LocatorsMainPage.LOGIN_BUTTON])
    def test_login_by_click_on_buttons_on_main_page(self, driver, button):
        driver.find_element(*button).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsLoginPage.TEXT_LOGIN, 'Вход'))
        driver.find_element(*LocatorsLoginPage.LOGIN_EMAIL_INPUT).send_keys(*AuthTestData.AUTH_EMAIL)
        driver.find_element(*LocatorsLoginPage.LOGIN_PASSWORD_INPUT).send_keys(*AuthTestData.AUTH_PASSWORD)
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        driver.find_element(*LocatorsMainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsAccountPage.PROFILE_BUTTON, 'Профиль'))
        assert driver.current_url == config.URL + config.ACCOUNT_PAGE

    # Переход в личный кабинет
    def test_transition_to_account_page(self, driver, login):
        driver.find_element(*LocatorsMainPage.ACCOUNT_BUTTON).click()
        assert driver.current_url == config.URL + config.ACCOUNT_PAGE

    #Переход к разделу "Булки"
    def test_transition_to_section_rolls(self, driver):
        driver.find_element(*LocatorsMainPage.BUTTON_FILLINGS).click()
        driver.find_element(*LocatorsMainPage.BUTTON_ROLLS).click()
        text_rolls = WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.visibility_of_element_located(LocatorsMainPage.TEXT_ROLLS))
        assert text_rolls.is_displayed()

    #Переход к разделу "Соусы"
    def test_transition_to_section_sauces(self, driver):
        driver.find_element(*LocatorsMainPage.BUTTON_SAUCES).click()
        text_sauces = WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.visibility_of_element_located(LocatorsMainPage.TEXT_SAUCES))
        assert text_sauces.is_displayed()

    #Переход к разделу "Начинки"
    def test_transition_to_section_fillings(self, driver):
        driver.find_element(*LocatorsMainPage.BUTTON_FILLINGS).click()
        text_fillings = WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.visibility_of_element_located(LocatorsMainPage.TEXT_FILLINGS))
        assert text_fillings.is_displayed()