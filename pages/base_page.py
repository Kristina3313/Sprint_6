from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_and_click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                         message=f'Element not found or not clickable in {locator}')
        element.click()

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Elements not found in {locator}')

    def wait_and_get_attribute(self, locator, attribute, time=20):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def choose_option_from_dropdown(self, field_locator, option_locator):
        self.driver.find_element(*field_locator).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(option_locator))
        self.driver.find_element(*option_locator).click()
