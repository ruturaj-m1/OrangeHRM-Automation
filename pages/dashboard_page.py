"""Dashboard page — landing page after successful login."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    USER_DROPDOWN = (By.CSS_SELECTOR, "span.oxd-userdropdown-tab")
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")

    # Sidebar menu (reused across module pages)
    MENU = staticmethod(lambda name: (By.XPATH, f"//span[normalize-space()='{name}']"))

    def go_to(self, module: str):
        """Click a left-side menu item: Admin, PIM, Leave, Time, Recruitment, My Info, etc."""
        self.click(self.MENU(module))

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT)

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)
