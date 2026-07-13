"""Recruitment module."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RecruitmentPage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='Recruitment']")
    CANDIDATES_TAB = (By.XPATH, "//a[normalize-space()='Candidates']")
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def open_candidates(self):
        self.click(self.CANDIDATES_TAB)

    def has_add_button(self) -> bool:
        return self.is_visible(self.ADD_BTN)
