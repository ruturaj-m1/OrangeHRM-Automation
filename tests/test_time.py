"""Time module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.time_page import TimePage


@pytest.mark.time
def test_time_page_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Time")
    assert TimePage(logged_in_driver).is_loaded()
