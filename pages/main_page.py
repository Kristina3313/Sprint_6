from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.dzen_page_locators import LocatorsDzen
from locators.main_page_locators import LocatorsMain
from pages.base_page import BasePage


class MainPage(BasePage):
    pointer0 = LocatorsMain.POINTER0
    pointer1 = LocatorsMain.POINTER1
    pointer2 = LocatorsMain.POINTER2
    pointer3 = LocatorsMain.POINTER3
    pointer4 = LocatorsMain.POINTER4
    pointer5 = LocatorsMain.POINTER5
    pointer6 = LocatorsMain.POINTER6
    pointer7 = LocatorsMain.POINTER7
    button_cookie = LocatorsMain.BUTTON_COOKIE
    logo_samokat = LocatorsMain.LOGO_SAMOKAT
    logo_yandex = LocatorsMain.LOGO_YANDEX
    card_news = LocatorsDzen.CARD_NEWS

    # клик на принятие куки
    @allure.step('Click to botton with cookie')
    def click_button_cookie(self):
        self.find_and_click_element(self.button_cookie)

    # метод скроллит до последнего элемента
    @allure.step('Scroll to last pointer')
    def scroll_to_pointer(self):
        element = self.find_element(self.pointer7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод кликает по кнопке "Сколько это стоит? И как оплатить?"
    @allure.step('Click to pointer0')
    def click_pointer0(self):
        self.find_and_click_element(self.pointer0)

    # метод кликает по кнопке "Хочу сразу несколько самокатов! Так можно?"
    @allure.step('Click to pointer1')
    def click_pointer1(self):
        self.find_and_click_element(self.pointer1)

    # метод кликает по кнопке "Как рассчитывается время аренды?"
    @allure.step('Click to pointer2')
    def click_pointer2(self):
        self.find_and_click_element(self.pointer2)

    # метод кликает по кнопке "Можно ли заказать самокат прямо на сегодня?"
    @allure.step('Click to pointer3')
    def click_pointer3(self):
        self.find_and_click_element(self.pointer3)

    # метод кликает по кнопке "Можно ли продлить заказ или вернуть самокат раньше?"
    @allure.step('Click to pointer4')
    def click_pointer4(self):
        self.find_and_click_element(self.pointer4)

    # метод кликает по кнопке "Вы привозите зарядку вместе с самокатом?"
    @allure.step('Click to pointer5')
    def click_pointer5(self):
        self.find_and_click_element(self.pointer5)

    # метод кликает по кнопке "Можно ли отменить заказ?"
    @allure.step('Click to pointer6')
    def click_pointer6(self):
        self.find_and_click_element(self.pointer6)

    # метод кликает по кнопке "Я живу за МКАДом, привезёте?"
    @allure.step('Click to pointer7')
    def click_pointer7(self):
        self.find_and_click_element(self.pointer7)

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer0
    @allure.step('Check information under pointer0')
    def check_under_pointer0(self):
        return self.wait_and_get_attribute(self.pointer0, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer1
    @allure.step('Check information under pointer1')
    def check_under_pointer1(self):
        return self.wait_and_get_attribute(self.pointer1, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer2
    @allure.step('Check information under pointer2')
    def check_under_pointer2(self):
        return self.wait_and_get_attribute(self.pointer2, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer3
    @allure.step('Check information under pointer3')
    def check_under_pointer3(self):
        return self.wait_and_get_attribute(self.pointer3, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer4
    @allure.step('Check information under pointer4')
    def check_under_pointer4(self):
        return self.wait_and_get_attribute(self.pointer4, 'aria-disabled')

#    метод проверяет, открылся ли элемент с текстом под стрелкой для pointer5
    @allure.step('Check information under pointer5')
    def check_under_pointer5(self):
        return self.wait_and_get_attribute(self.pointer5, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer6
    @allure.step('Check information under pointer6')
    def check_under_pointer6(self):
        return self.wait_and_get_attribute(self.pointer6, 'aria-disabled')

    # метод проверяет, открылся ли элемент с текстом под стрелкой для pointer7
    @allure.step('Check information under pointer7')
    def check_under_pointer7(self):
        return self.wait_and_get_attribute(self.pointer7, 'aria-disabled')

    # метод кликает на лого "Самокат"
    @allure.step('Click to logo Samokat')
    def click_to_samokat_logo(self):
        self.find_and_click_element(self.logo_samokat)

    # метод кликает на лого "Яндекс" и переключается на новую вкладку
    @allure.step('Click to logo Yandex')
    def click_to_yandex_logo(self, current_url=None):
        main_window_handle = self.driver.current_window_handle
        self.find_and_click_element(self.logo_yandex)
        WebDriverWait(self.driver, 20).until(lambda driver: len(self.driver.window_handles) > 1)
        # Переключаемся на новую вкладку
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.card_news))
