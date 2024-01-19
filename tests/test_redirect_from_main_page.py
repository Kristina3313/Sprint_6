import allure
from conftest import driver
from pages.dzen_page import DzenPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.story('Тест редиректов по кликам на лого')
class TestRedirectFromMainPage:
    @allure.title('Тест клика на лого Самоката')
    def test_click_logo_positive(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(driver)
        order_page.click_order_button_from_header()
        main_page.click_to_samokat_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Тест клика на лого Яндекс')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_yandex_logo()
        dzen_page = DzenPage(driver)
        text_from_card = dzen_page.get_elements_news()
        assert any('Новости' in item for item in text_from_card)
