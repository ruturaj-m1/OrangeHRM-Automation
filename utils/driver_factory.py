"""Creates a Selenium WebDriver based on the requested browser.

Uses `webdriver-manager` so users don't need to download drivers manually.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.config_reader import CONFIG
from utils.logger import get_logger

log = get_logger(__name__)


class DriverFactory:
    """Factory that returns a ready-to-use WebDriver instance."""

    @staticmethod
    def get_driver(browser: str | None = None):
        browser = (browser or CONFIG["browser"]["default"]).lower()
        headless = CONFIG["browser"]["headless"]
        w, h = CONFIG["browser"]["window_size"].split(",")

        log.info(f"Launching {browser} (headless={headless})")

        if browser == "chrome":
            opts = ChromeOptions()
            if headless:
                opts.add_argument("--headless=new")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
            opts.add_argument("--disable-gpu")
            opts.add_argument(f"--window-size={w},{h}")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

        elif browser == "firefox":
            opts = FirefoxOptions()
            if headless:
                opts.add_argument("-headless")
            opts.add_argument(f"--width={w}")
            opts.add_argument(f"--height={h}")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)

        elif browser == "edge":
            opts = EdgeOptions()
            if headless:
                opts.add_argument("--headless=new")
            opts.add_argument("--no-sandbox")
            opts.add_argument(f"--window-size={w},{h}")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opts)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(CONFIG["timeouts"]["implicit"])
        driver.set_page_load_timeout(CONFIG["timeouts"]["page_load"])
        return driver
