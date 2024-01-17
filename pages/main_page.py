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
    text0 = LocatorsMain.TEXT_UNDER_POINTER0
    text1 = LocatorsMain.TEXT_UNDER_POINTER1
    text2 = LocatorsMain.TEXT_UNDER_POINTER2
    text3 = LocatorsMain.TEXT_UNDER_POINTER3
    text4 = LocatorsMain.TEXT_UNDER_POINTER4
    text5 = LocatorsMain.TEXT_UNDER_POINTER5
    text6 = LocatorsMain.TEXT_UNDER_POINTER6
    text7 = LocatorsMain.TEXT_UNDER_POINTER7

    @allure.step('Клик на кнопку принятия куки')
    def click_button_cookie(self):
        self.find_and_click_element(self.button_cookie)

    @allure.step('Скролл до последней стрелки')
    def scroll_to_pointer(self):
        self.scroll_into_view(self.pointer7)

    @allure.step('Клик по стрелке "Сколько это стоит? И как оплатить?"')
    def click_pointer0(self):
        self.find_and_click_element(self.pointer0)

    @allure.step('Клик по стрелке "Хочу сразу несколько самокатов! Так можно?"')
    def click_pointer1(self):
        self.find_and_click_element(self.pointer1)

    @allure.step('Клик по стрелке "Как рассчитывается время аренды?"')
    def click_pointer2(self):
        self.find_and_click_element(self.pointer2)

    @allure.step('Клик по стрелке "Можно ли заказать самокат прямо на сегодня?"')
    def click_pointer3(self):
        self.find_and_click_element(self.pointer3)

    @allure.step('Клик по стрелке "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_pointer4(self):
        self.find_and_click_element(self.pointer4)

    @allure.step('Клик по стрелке "Вы привозите зарядку вместе с самокатом?"')
    def click_pointer5(self):
        self.find_and_click_element(self.pointer5)

    @allure.step('Клик по стрелке "Можно ли отменить заказ?"')
    def click_pointer6(self):
        self.find_and_click_element(self.pointer6)

    @allure.step('Клик по стрелке "Я живу за МКАДом, привезёте?"')
    def click_pointer7(self):
        self.find_and_click_element(self.pointer7)

    @allure.step('Получение текста под стрелкой 0')
    def get_text_under_pointer0(self):
        return self.get_text_from_element(self.text0)

    @allure.step('Получение текста под стрелкой 1')
    def get_text_under_pointer1(self):
        return self.get_text_from_element(self.text1)

    @allure.step('Получение текста под стрелкой 2')
    def get_text_under_pointer2(self):
        return self.get_text_from_element(self.text2)

    @allure.step('Получение текста под стрелкой 3')
    def get_text_under_pointer3(self):
        return self.get_text_from_element(self.text3)

    @allure.step('Получение текста под стрелкой 4')
    def get_text_under_pointer4(self):
        return self.get_text_from_element(self.text4)

    @allure.step('Получение текста под стрелкой 5')
    def get_text_under_pointer5(self):
        return self.get_text_from_element(self.text5)

    @allure.step('Получение текста под стрелкой 6')
    def get_text_under_pointer6(self):
        return self.get_text_from_element(self.text6)

    @allure.step('Получение текста под стрелкой 7')
    def get_text_under_pointer7(self):
        return self.get_text_from_element(self.text7)

    @allure.step('Клик на лого "Самокат')
    def click_to_samokat_logo(self):
        self.click_to_logo(self.logo_samokat)

    @allure.step('Клик на лого Яндекс и переключение на новую вкладку')
    def click_to_yandex_logo(self):
        self.click_to_logo(self.logo_yandex)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)
