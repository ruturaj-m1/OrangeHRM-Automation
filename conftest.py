"""PyTest fixtures & hooks — driver setup, screenshots on failure, HTML report attachment."""
import os
from datetime import datetime

import pytest

from utils.config_reader import CONFIG, TEST_DATA
from utils.driver_factory import DriverFactory
from utils.logger import get_logger
from pages.login_page import LoginPage

log = get_logger("conftest")

SCREENSHOT_DIR = CONFIG["paths"]["screenshots"]
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests on: chrome | firefox | edge",
    )


@pytest.fixture(scope="session")
def config():
    return CONFIG


@pytest.fixture(scope="session")
def test_data():
    return TEST_DATA


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    drv = DriverFactory.get_driver(browser)
    request.node._driver = drv  # exposed to the hook below for screenshots
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver, test_data):
    """Convenience fixture — returns a driver already logged into OrangeHRM."""
    login = LoginPage(driver)
    login.load()
    login.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    assert login.is_logged_in(), "Precondition failed: could not log in"
    return driver


# ---- Screenshot on failure + attach to HTML report ----
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = getattr(item, "_driver", None)
        if drv is not None:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = f"{item.name}_{ts}.png"
            path = os.path.join(SCREENSHOT_DIR, fname)
            try:
                drv.save_screenshot(path)
                log.error(f"Test failed. Screenshot: {path}")
                # attach to pytest-html report if available
                extras = getattr(report, "extras", [])
                try:
                    from pytest_html import extras as html_extras
                    extras.append(html_extras.image(path))
                    report.extras = extras
                except Exception:
                    pass
            except Exception as e:
                log.error(f"Could not capture screenshot: {e}")
