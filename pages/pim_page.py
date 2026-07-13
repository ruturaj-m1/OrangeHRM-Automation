"""PIM module — Personal Information Management."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PIMPage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='PIM']")
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BTN = (By.XPATH, "//button[normalize-space()='Save']")
    PERSONAL_DETAILS = (By.XPATH, "//h6[normalize-space()='Personal Details']")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def add_employee(self, first: str, middle: str, last: str):
        self.click(self.ADD_BTN)
        self.type(self.FIRST_NAME, first)
        self.type(self.MIDDLE_NAME, middle)
        self.type(self.LAST_NAME, last)
        self.click(self.SAVE_BTN)

    def is_employee_created(self) -> bool:
        return self.is_visible(self.PERSONAL_DETAILS)
