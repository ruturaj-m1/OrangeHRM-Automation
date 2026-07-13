"""Admin module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


@pytest.mark.admin
def test_admin_page_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Admin")
    assert AdminPage(logged_in_driver).is_loaded()


@pytest.mark.admin
def test_admin_search_user(logged_in_driver, test_data):
    DashboardPage(logged_in_driver).go_to("Admin")
    admin = AdminPage(logged_in_driver)
    admin.search_user(test_data["search"]["admin_username"])
    assert admin.result_count() >= 1
