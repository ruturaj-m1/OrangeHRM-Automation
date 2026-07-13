"""My Info module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@pytest.mark.myinfo
def test_my_info_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("My Info")
    my_info = MyInfoPage(logged_in_driver)
    assert my_info.is_loaded()
    assert my_info.get_first_name() != ""
