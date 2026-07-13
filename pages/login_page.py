"""Login page object."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_reader import CONFIG


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, "div.oxd-alert-content--error p")
    DASHBOARD_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def load(self):
        self.open(CONFIG["app"]["base_url"] + CONFIG["app"]["login_path"])

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.DASHBOARD_HEADER)

    def get_error(self) -> str:
        return self.get_text(self.ERROR_MSG)
