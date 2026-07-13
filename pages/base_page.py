"""Base Page — every page object extends this class.

Contains reusable Selenium wrappers with explicit waits and logging.
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_reader import CONFIG
from utils.logger import get_logger


class BasePage:
    """Reusable wrappers around Selenium with explicit waits."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = CONFIG["timeouts"]["explicit"]
        self.log = get_logger(self.__class__.__name__)

    # ---------- Navigation ----------
    def open(self, url: str):
        self.log.info(f"Opening URL: {url}")
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def current_url(self) -> str:
        return self.driver.current_url

    # ---------- Wait helpers ----------
    def _wait(self):
        return WebDriverWait(self.driver, self.timeout)

    def wait_visible(self, locator: tuple[str, str]):
        return self._wait().until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple[str, str]):
        return self._wait().until(EC.element_to_be_clickable(locator))

    def wait_url_contains(self, text: str) -> bool:
        try:
            return self._wait().until(EC.url_contains(text))
        except TimeoutException:
            return False

    # ---------- Actions ----------
    def click(self, locator: tuple[str, str]):
        self.log.info(f"Click: {locator}")
        self.wait_clickable(locator).click()

    def type(self, locator: tuple[str, str], text: str, clear: bool = True):
        self.log.info(f"Type into {locator}: {text!r}")
        el = self.wait_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.wait_visible(locator).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    # ---------- Utility ----------
    def take_screenshot(self, path: str):
        self.driver.save_screenshot(path)
        self.log.info(f"Screenshot saved: {path}")
