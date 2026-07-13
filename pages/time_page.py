"""Time module."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TimePage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='Time']")
    TIMESHEETS_TAB = (By.XPATH, "//a[normalize-space()='Timesheets']")
    MY_TIMESHEET = (By.XPATH, "//a[normalize-space()='My Timesheets']")

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def open_my_timesheet(self):
        self.click(self.TIMESHEETS_TAB)
        self.click(self.MY_TIMESHEET)
