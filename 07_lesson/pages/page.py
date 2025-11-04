from selenium.webdriver.common.by import By

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        user_input = self.find_element(By.ID, 'user-name')
        user_input.send_keys(username)

    def enter_password(self, password):
        pass_input = self.find_element(By.ID, 'password')
        pass_input.send_keys(password)

    def click_login_button(self):
        login_btn = self.find_element(By.CLASS_NAME, 'btn_action')
        login_btn.click()

class ProductPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart_by_name(self, product_name):
        element = self.find_element(By.XPATH, f"//div[contains(@class,'inventory_item_name')][normalize-space()='{product_name}']")
        parent_div = element.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']")
        add_to_cart_button = parent_div.find_element(By.CLASS_NAME, 'btn_inventory')
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_link = self.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_link.click()

class CartPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        checkout_button = self.find_element(By.CLASS_NAME, 'checkout_button')
        checkout_button.click()

class CheckoutStepOnePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_name(self, first_name_value):
        first_name_field = self.find_element(By.ID, 'first-name')
        first_name_field.send_keys(first_name_value)

    def fill_last_name(self, last_name_value):
        last_name_field = self.find_element(By.ID, 'last-name')
        last_name_field.send_keys(last_name_value)

    def fill_postal_code(self, postal_code_value):
        postal_code_field = self.find_element(By.ID, 'postal-code')
        postal_code_field.send_keys(postal_code_value)

    def continue_checkout(self):
        continue_button = self.find_element(By.CLASS_NAME, 'cart_button')
        continue_button.click()

class CheckoutOverviewPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def get_total_price(self):
        total_text = self.find_element(By.CLASS_NAME, 'summary_total_label').text
        return float(total_text.split(':')[1].strip().replace('$', ''))