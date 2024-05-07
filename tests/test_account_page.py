import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config
from locators import LocatorsAccountPage, LocatorsLoginPage


class TestAccountPage:
    #Переход из ЛК к конструктору по клику на кнопку "Конструктор" и лого Stellar Burgers.
    @pytest.mark.parametrize('link', [LocatorsAccountPage.CONSTRUCTOR_BUTTON, LocatorsAccountPage.LOGO_SB])
    def test_transition_to_constructor_by_click_on_the_links(self, driver, login, link):
        driver.find_element(*link).click()
        assert driver.current_url == config.URL + config.MAIN_PAGE

    #Выход из ЛК по кнопке "Выйти" в личном кабинете.
    def test_logout_of_the_account(self, driver, login):
        driver.find_element(*LocatorsAccountPage.LOGOUT_BUTTON).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsLoginPage.TEXT_LOGIN, 'Вход'))
        text_login = driver.find_element(*LocatorsLoginPage.TEXT_LOGIN).text
        assert text_login == 'Вход'