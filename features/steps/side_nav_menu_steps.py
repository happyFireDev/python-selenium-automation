from behave import when
from selenium.webdriver.common.by import By
from pages.side_nav_menu import SideNavMenu
from pages.base_page import Page


@when('Click on sign-in for right side navigation menu')
def click_sign_in_btn_side_nav(context):
    context.app.side_nav_menu.click_sign_in_btn_side_nav()


@when('Click Add to Cart in side-menu pop-up')
def click_add_to_cart(context):
    context.app.side_nav_menu.click_side_nav_add_to_cart_btn()

