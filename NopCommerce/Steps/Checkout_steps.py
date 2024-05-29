from behave import given, when, then
from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckoutPage


@given('I am on the homepage')
def step_given_on_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.nopcommerce.com/")
    context.homepage = HomePage(context.driver)


@when('I add an item to the cart')
def step_when_add_item_to_cart(context):
    context.homepage.click_add_to_cart_featured_product_htc_one_m8()


@when('I go to the cart')
def step_when_go_to_cart(context):
    context.homepage.click_shopping_cart()
    context.cart_page = CartPage(context.driver)


@when('I click on checkout')
def step_when_click_on_checkout(context):
    context.cart_page.click_checkout_button()
    context.checkout_page = CheckoutPage(context.driver)


@when('I log in with valid credentials')
def step_when_log_in(context):
    context.checkout_page.login_as_registered_user("user@example.com", "password")


@then('I should be able to complete the checkout process')
def step_then_complete_checkout(context):
    context.checkout_page.complete_checkout()
    context.driver.quit()
