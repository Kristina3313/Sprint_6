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

    @allure.step('Клик по стрелке')
    def click_pointer(self, pointer_index):
        pointer_locator = getattr(self, f'pointer{pointer_index}')
        self.find_and_click_element(pointer_locator)

    @allure.step('Получение текста под стрелкой')
    def get_text_under_pointer(self, pointer_index):
        text_locator = getattr(self, f'text{pointer_index}')
        return self.get_text_from_element(text_locator)

    @allure.step('Клик на лого "Самокат')
    def click_to_samokat_logo(self):
        self.click_to_logo(self.logo_samokat)

    @allure.step('Клик на лого Яндекс и переключение на новую вкладку')
    def click_to_yandex_logo(self):
        self.click_to_logo(self.logo_yandex)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)
