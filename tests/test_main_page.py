import allure
import pytest
from pages.dzen_page import DzenPage
from pages.main_page import MainPage
from conftest import driver
from pages.order_page import OrderPage


@allure.story("Test information from underpoiners")
class TestMainPointer:
    @pytest.mark.parametrize("pointer_num", range(8))
    @allure.title("Тest get status under pointer{pointer_num}")
    def test_click_pointer(self, driver, pointer_num):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        getattr(main_page, f"click_pointer{pointer_num}")()
        pointer_after_click = getattr(main_page, f"check_under_pointer{pointer_num}")()
        assert pointer_after_click == "true"

    @allure.story('Test redirect from logo')
    class TestRedirect:
        @allure.title('Test redirect after click to Logo Samokat')
        # проверка клика на логотип самоката (должен произойти переход на главную страницу Самоката)
        def test_click_logo_positive(self, driver):
            main_page = MainPage(driver)
            main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
            order_page = OrderPage(driver)
            order_page.click_order_button_from_header()
            main_page.click_to_samokat_logo()
            assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        @allure.title('Test redirect after click to Logo Yandex')
        # проверка клика на логотип Яндекса (должна открыться главная страница Дзена)
        def test_click_yandex_logo(self, driver):
            main_page = MainPage(driver)
            main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
            main_page.click_to_yandex_logo()
            dzen_page = DzenPage(driver)
            text_from_card = dzen_page.get_elements_news()
            assert any('Новости' in item for item in text_from_card)
