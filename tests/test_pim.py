"""PIM module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


@pytest.mark.pim
def test_pim_page_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("PIM")
    assert PIMPage(logged_in_driver).is_loaded()


@pytest.mark.pim
def test_add_employee(logged_in_driver, test_data):
    DashboardPage(logged_in_driver).go_to("PIM")
    pim = PIMPage(logged_in_driver)
    emp = test_data["new_employee"]
    pim.add_employee(emp["first_name"], emp["middle_name"], emp["last_name"])
    assert pim.is_employee_created()
