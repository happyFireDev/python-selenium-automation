from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideNavMenu(Page):

    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIGN_IN_BTN_RIGHT_NAV = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def click_sign_in_btn_side_nav(self):
        self.wait_until_clickable(*self.SIGN_IN_BTN_RIGHT_NAV)
        self.click(*self.SIGN_IN_BTN_RIGHT_NAV)

    def click_side_nav_add_to_cart_btn(self):
        #self.wait_until_clickable(self.SIDE_NAV_ADD_TO_CART_BTN)

        # ✅ Wait for the entire side-nav panel to appear
        self.wait.until(
            EC.presence_of_element_located(self.SIDE_NAV_ADD_TO_CART_BTN),
            message=f'Expected {self.SIDE_NAV_ADD_TO_CART_BTN} to be present in the cart section'
        )

        self.click(*self.SIDE_NAV_ADD_TO_CART_BTN)
        print('The SIDE_NAV_ADD_TO_CART_BTN details are: ', self.SIDE_NAV_ADD_TO_CART_BTN)


    # def store_product_name(self, context):
    #     print('SIDE_NAV_PRODUCT_NAME type:', type(self.SIDE_NAV_PRODUCT_NAME))
    #     print('SIDE_NAV_PRODUCT_NAME:', *self.SIDE_NAV_PRODUCT_NAME)
    #     print('SIDE_NAV_PRODUCT_NAME - no * :', self.SIDE_NAV_PRODUCT_NAME)
    #
    #     # ✅ Wait for the entire side-nav panel to appear
    #     self.wait_until_visible(*self.SIDE_NAV_PRODUCT_NAME)
    #
    #     # 🔁 Re-find it once it's present
    #     element = self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
    #
    #     context.product_name = element.text.strip()
    #
    #     print('Product name stored:', context.product_name)
    #
    #     assert context.product_name, "Product name was empty!"
    #
    #     return context.product_name

    def store_product_name(self, context):
        print('SIDE_NAV_PRODUCT_NAME type:', type(self.SIDE_NAV_PRODUCT_NAME))
        print('SIDE_NAV_PRODUCT_NAME:', *self.SIDE_NAV_PRODUCT_NAME)

        # ✅ Wait for the cart side-panel first
        side_nav_panel = (By.CSS_SELECTOR, "[data-test='content-wrapper']")
        self.wait_until_visible(*side_nav_panel)
        print("✅ Side nav container is visible")

        # 💡 Take a screenshot for confirmation
        # self.driver.save_screenshot("side_nav_panel_open.png")

        # ✅ Now wait for the actual product name to appear
        self.wait_until_visible(*self.SIDE_NAV_PRODUCT_NAME)

        element = self.find_element(*self.SIDE_NAV_PRODUCT_NAME)
        context.product_name = element.text.strip()
        print('✅ Product name stored:', context.product_name)

        assert context.product_name, "❌ Product name was empty!"
        return context.product_name
