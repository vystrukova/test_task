from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER = (By.CSS_SELECTOR, ".spinner")

    MAIN_SEARCH_BUTTON = (By.XPATH, "//span[@class='supernova-search-submit-text']")
    MAIN_SEARCH_INPUT = (By.XPATH, "//input[@id='a11y-search-input'][1]")
    MAIN_LOGIN_BUTTON = (By.XPATH, "//a[@class='supernova-button']")


class LoginPageLocators(BasePageLocators):
    LOGIN_WITH_PASS = (By.XPATH, "//button[@data-qa='expand-login-by-password']")
    LOGIN_USERNAME = (By.XPATH, "//input[@placeholder='Электронная почта или телефон']")
    LOGIN_PASS = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='account-login-submit']")
    LOGIN_MY_RESUMES = (By.XPATH, "//a[@data-qa='mainmenu_myResumes']")


class SearchPageLocators(BasePageLocators):
    SEARCH_INPUT = (By.XPATH, "//input[@id='a11y-search-input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-qa='search-button']")