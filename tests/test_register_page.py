from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import config
from data import AuthTestData, UserTestDataGenerator
from locators import LocatorsAccountPage, LocatorsLoginPage, LocatorsMainPage, LocatorsRegisterPage


user_test_data = UserTestDataGenerator.generator()

class TestRegisterPage:
    #Успешная регистрация.
    def test_successful_registration(self, driver):
        driver.get(config.URL + config.REGISTER_PAGE)
        name_input = driver.find_element(*LocatorsRegisterPage.REG_NAME_INPUT)
        name_input.send_keys(user_test_data['name'])
        email_input = driver.find_element(*LocatorsRegisterPage.REG_EMAIL_INPUT)
        email_input.send_keys(user_test_data['email'])
        password_input = driver.find_element(*LocatorsRegisterPage.REG_PASSWORD_INPUT)
        password_input.send_keys(user_test_data['password'])
        submit_button = driver.find_element(*LocatorsRegisterPage.REG_BUTTON)
        submit_button.click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsLoginPage.TEXT_LOGIN, 'Вход'))
        assert driver.find_element(*LocatorsLoginPage.TEXT_LOGIN).is_displayed()

    #Ошибка регистрации при некорректном пароле.
    def test_error_registration_when_the_password_is_less_than_6_symbols(self, driver):
        driver.get(config.URL + config.REGISTER_PAGE)
        name_input = driver.find_element(*LocatorsRegisterPage.REG_NAME_INPUT)
        name_input.send_keys(user_test_data['name'])
        email_input = driver.find_element(*LocatorsRegisterPage.REG_EMAIL_INPUT)
        email_input.send_keys(user_test_data['email'])
        password_input = driver.find_element(*LocatorsRegisterPage.REG_PASSWORD_INPUT)
        password_input.send_keys(*AuthTestData.INCORRECT_PASSWORD)
        submit_button = driver.find_element(*LocatorsRegisterPage.REG_BUTTON)
        submit_button.click()
        assert driver.find_element(*LocatorsRegisterPage.REG_ERROR_TEXT).is_displayed()

    #Вход в ЛК по ссылке на странице регистрации.
    def test_login_by_click_on_link_in_register_page(self, driver):
        driver.get(config.URL + config.REGISTER_PAGE)
        driver.find_element(*LocatorsRegisterPage.LOGIN_LINK).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsLoginPage.TEXT_LOGIN, 'Вход'))
        driver.find_element(*LocatorsLoginPage.LOGIN_EMAIL_INPUT).send_keys(*AuthTestData.AUTH_EMAIL)
        driver.find_element(*LocatorsLoginPage.LOGIN_PASSWORD_INPUT).send_keys(*AuthTestData.AUTH_PASSWORD)
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        driver.find_element(*LocatorsMainPage.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, config.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(LocatorsAccountPage.PROFILE_BUTTON, 'Профиль'))
        assert driver.current_url == config.URL + config.ACCOUNT_PAGE