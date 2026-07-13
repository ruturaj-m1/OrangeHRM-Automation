"""Admin module page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminPage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='Admin']")
    USERNAME_INPUT = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_ROWS = (By.CSS_SELECTOR, "div.oxd-table-card")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def search_user(self, username: str):
        self.type(self.USERNAME_INPUT, username)
        self.click(self.SEARCH_BTN)

    def result_count(self) -> int:
        # small pause via explicit wait on at least the header
        return len(self.driver.find_elements(*self.RESULT_ROWS))
