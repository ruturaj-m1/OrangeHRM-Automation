"""Login module tests."""
import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver, test_data):
    login = LoginPage(driver)
    login.load()
    login.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    assert login.is_logged_in(), "User should be logged in and see the Dashboard"


@pytest.mark.login
def test_invalid_login(driver, test_data):
    login = LoginPage(driver)
    login.load()
    login.login(test_data["invalid_user"]["username"], test_data["invalid_user"]["password"])
    assert "Invalid credentials" in login.get_error()
