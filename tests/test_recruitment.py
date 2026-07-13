"""Recruitment module tests."""
import pytest

from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage


@pytest.mark.recruitment
def test_recruitment_page_loads(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Recruitment")
    assert RecruitmentPage(logged_in_driver).is_loaded()


@pytest.mark.recruitment
def test_candidates_tab(logged_in_driver):
    DashboardPage(logged_in_driver).go_to("Recruitment")
    rec = RecruitmentPage(logged_in_driver)
    rec.open_candidates()
    assert rec.has_add_button()
