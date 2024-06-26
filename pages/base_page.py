from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_and_click_element(self, locator, time=20):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                         message=f'Element not found or not clickable in {locator}')
        element.click()

    def find_elements_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Elements not found in {locator}')

    def wait_and_get_attribute(self, locator, attribute, time=30):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def choose_option_from_dropdown(self, field_locator, option_locator):
        self.driver.find_element(*field_locator).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(option_locator))
        self.driver.find_element(*option_locator).click()

    def switch_to_new_tab(self, main_window_handle, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda driver: len(self.driver.window_handles) > 1)
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_from_element(self, locator, time=20):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                         message=f'Element not found in {locator}')
        return element.text

    def click_to_logo(self, logo_locator):
        self.find_and_click_element(logo_locator)
