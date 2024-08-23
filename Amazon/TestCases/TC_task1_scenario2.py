import time

import pytest
from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
from PageObjects.TodaysDealsPage import TodaysDealsPage
from UTILS.write_xlsx import XlsxWriter
import sys
import os
from pathlib import Path

parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "UTILS")
sys.path.append(TB_Path)


@pytest.fixture(scope="module")
def setup_browser():
    driver = webdriver.Firefox()
    driver.set_window_size(1024, 768)
    driver.get("https://www.amazon.com/")
    homepage = HomePage(driver)
    yield homepage
    driver.quit()


def test_01_navigate_to_todays_deals(setup_browser):
    homepage = setup_browser
    homepage.go_to_today_deals_page()
    deals_page = TodaysDealsPage(homepage.driver)
    try:
        assert "Deals" in deals_page.driver.title
        XlsxWriter.write_task1_scene2_sheet('TC_01', "Successfully navigated to Today's deals page", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene2_sheet('TC_01', "Error! to navigate to the page", 'Fail', '')
        raise


def test_02_apply_filters(setup_browser):
    homepage = setup_browser
    filters_to_be_applied = ['Electronics', '10% off or more', '200 &']
    homepage.go_to_today_deals_page()
    deals_page = TodaysDealsPage(homepage.driver)
    deals_page.expand_more_options()
    for filters in filters_to_be_applied:
        deals_page.apply_filter_name(filters)
    try:
        for check_filter in filters_to_be_applied:
            assert deals_page.verify_applied_filter(check_filter), f"Filter '{check_filter}' was not applied"
        XlsxWriter.write_task1_scene2_sheet('TC_02', "All filters added successfully", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene2_sheet('TC_02', "Error! in adding filters", 'Fail', '')
        raise


def test_03_add_random_item_page_four_scenario_test(setup_browser):
    homepage = setup_browser
    filters_to_be_applied = ['Books', '10% off or more', 'Under $25']
    homepage.go_to_today_deals_page()
    deals_page = TodaysDealsPage(homepage.driver)
    deals_page.expand_more_options()
    for filters in filters_to_be_applied:
        deals_page.apply_filter_name(filters)
    time.sleep(2)
    deals_page.scroll_number_of_pages(4)
    try:
        deals_page.add_item_to_cart()
        assert deals_page.verify_item_added_to_cart()
        XlsxWriter.write_task1_scene2_sheet('TC_03', "Navigated to fourth page and item added successfully", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene2_sheet('TC_03', "Error!", 'Fail', '')
        raise
