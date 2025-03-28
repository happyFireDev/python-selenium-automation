from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page


@when('Click on sign-in button')
def click_sign_in_button(context):
    context.app.header.click_sign_in()


@when('Click on shopping cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)

