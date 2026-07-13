"""Leave module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage


@pytest.mark.leave
def test_leave_page_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Leave")
    assert LeavePage(logged_in_driver).is_loaded()


@pytest.mark.leave
def test_open_apply_leave(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Leave")
    leave = LeavePage(logged_in_driver)
    leave.open_apply()
    assert leave.is_apply_open()
