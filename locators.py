from selenium.webdriver.common.by import By


class LocatorsRegisterPage:
    REG_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  #Поле "Имя".
    REG_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  #Поле "Email".
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  #Поле "Пароль".
    REG_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  #Кнопка "Зарегистрироваться".
    REG_ERROR_TEXT = (By.XPATH, "//p[@class = 'input__error text_type_main-default']") #Текст ошибки "Некорректный пароль".
    LOGIN_LINK = (By.XPATH, "//a[@href = '/login']")  #Ссылка "Войти".


class LocatorsLoginPage:
    TEXT_LOGIN = (By.XPATH, "//h2[text() = 'Вход']")  #Текст "Вход".
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name = 'name']")  #Поле "Email".
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  #Поле "Пароль".
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  #Кнопка "Войти".


class LocatorsMainPage:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  #Кнопка "Личный кабинет".
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  #Кнопка "Войти в аккаунт".
    BUTTON_ROLLS = (By.XPATH, "//span[text() = 'Булки']")  #Кнопка "Булки" для перехода к булкам.
    BUTTON_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")  #Кнопка "Соусы" для перехода к соусам.
    BUTTON_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")  #Кнопка "Начинки" для перехода к начинкам.
    TEXT_ROLLS = (By.XPATH, "//h2[text() = 'Булки']")  #Текст раздела "Булки".
    TEXT_SAUCES = (By.XPATH, "//h2[text() = 'Соусы']")  #Текст раздела "Соусы".
    TEXT_FILLINGS = (By.XPATH, "//h2[text() = 'Начинки']")  #Текст раздела "Начинки".


class LocatorsForgotPasswordPage:
    LOGIN_LINK = (By.XPATH, "//a[@href = '/login']")  #Ссылка "Войти".


class LocatorsAccountPage:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li/a[@href = '/']")  #Кнопка "Конструктор".
    LOGO_SB = (By.XPATH, "//div/a[@href = '/']")  #Лого Stellar Burgers.
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account/profile']")  #Кнопка "Профиль".
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  #Кнопка "Выход".