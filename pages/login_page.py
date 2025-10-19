# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_BOX = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

    def _type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()
        el.clear()                 
        el.send_keys(text)

    def set_username(self, username):
        self._type(self.USERNAME, username)

    def set_password(self, password):
        self._type(self.PASSWORD, password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_error_text(self):
        
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_BOX))
            return el.text.strip()
        except TimeoutException:
            return ""

    def wait_until_inventory_loaded(self):
        
        self.wait.until(EC.url_contains("inventory.html"))

    def current_username_value(self):
       
        return self.driver.find_element(*self.USERNAME).get_attribute("value")
