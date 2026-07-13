"""My Info module."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyInfoPage(BasePage):
    HEADER = (By.XPATH, "//h6[contains(normalize-space(),'Personal Details')]")
    FIRST_NAME = (By.NAME, "firstName")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def get_first_name(self) -> str:
        return self.wait_visible(self.FIRST_NAME).get_attribute("value")
