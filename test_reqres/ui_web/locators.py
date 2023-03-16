from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER = (By.CSS_SELECTOR, ".spinner")
    LOGO_REQRES = (By.XPATH, "//a[@href='/']")
    LOGO_FAIL_REQRES = (By.XPATH, "//a[@href='123']")


class MainPageLocators(BasePageLocators):
    LIST_OF_ALL_REQUESTS = (By.XPATH, "//div[@class='endpoints']")
    FAKE_LIST_OF_ALL_REQUESTS = (By.XPATH, "//div[@class='endpoints']")

    LIST_USERS = (By.XPATH, "//li[@data-id='users']")
    SINGLE_USER = (By.XPATH, "//li[@data-id='users-single']")
    SINGLE_USER_NOT_FOUND = (By.XPATH, "//li[@data-id='users-single-not-found']")
    LIST_RESOURCE = (By.XPATH, "//li[@data-id='unknown']")
    SINGLE_RESOURCE = (By.XPATH, "//li[@data-id='unknown-single']")
    SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, "//li[@data-id='unknown-single-not-found']")
    POST_CREATE = (By.XPATH, "//li[@data-id='post']")
    PUT_UPDATE = (By.XPATH, "//li[@data-id='put']")
    PATCH_UPDATE = (By.XPATH, "//li[@data-id='patch']")
    DELETE_USER = (By.XPATH, "//li[@data-id='delete']")
    REGISTER_SUCCESSFUL = (By.XPATH, "//li[@data-id='register-successful']")
    REGISTER_UNSUCCESSFUL = (By.XPATH, "//li[@data-id='register-unsuccessful']")
    LOGIN_SUCCESSFUL = (By.XPATH, "//li[@data-id='login-successful']")
    LOGIN_UNSUCCESSFUL = (By.XPATH, "//li[@data-id='login-unsuccessful']")
    DELAYED_RESPONSE = (By.XPATH, "//li[@data-id='delay']")

    RESPONSE_CODE = (By.XPATH, "//span[@class='response-code']")
    JSON_TEXT = (By.CSS_SELECTOR, "pre[data-key='output-response']")