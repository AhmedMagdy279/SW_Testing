import pytest
from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
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


def test_01_search_car_accessories(setup_browser):
    homepage = setup_browser
    homepage.search_for_item('car accessories')
    try:
        assert "car accessories" in homepage.driver.title
        XlsxWriter.write_task1_scene1_sheet('TC_01', "The driver title is changed to 'car accessories'", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene1_sheet('TC_01', "Error to search for 'car accessories'", 'Fail', '')
        raise


def test_02_select_first_item(setup_browser):
    homepage = setup_browser
    homepage.search_for_item('car accessories')
    item_name = homepage.select_item_index_to_cart(1)
    try:
        assert homepage.verify_item_added_to_cart()
        XlsxWriter.write_task1_scene1_sheet('TC_02', "First Item added to cart successfully", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene1_sheet('TC_02', "Error to add item to cart", 'Fail', '')
        raise


def test_03_verify_item_in_cart_scenario_test(setup_browser):
    homepage = setup_browser
    homepage.search_for_item('car accessories')
    product_name = homepage.select_item_index_to_cart(1)
    cart_page = CartPage(homepage.driver)
    try:
        assert cart_page.check_item_in_cart(product_name)
        XlsxWriter.write_task1_scene1_sheet('TC_03', "Both items matched", 'Pass', '')
    except AssertionError:
        XlsxWriter.write_task1_scene1_sheet('TC_03', "Error! items aren't the same", 'Fail', '')
        raise
