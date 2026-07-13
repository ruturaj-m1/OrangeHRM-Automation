"""Leave module."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LeavePage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='Leave']")
    APPLY_TAB = (By.XPATH, "//a[normalize-space()='Apply']")
    APPLY_HEADER = (By.XPATH, "//h6[normalize-space()='Apply Leave']")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def open_apply(self):
        self.click(self.APPLY_TAB)

    def is_apply_open(self) -> bool:
        return self.is_visible(self.APPLY_HEADER)
