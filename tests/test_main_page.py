import allure
import pytest
from conftest import driver
from pages.dzen_page import DzenPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.story('Тест элементов на главной странице')
class TestMainPage:
    @allure.title("Тест проверки отображения текста под стрелкой")
    @pytest.mark.parametrize("pointer_index, expected_text", [
        (0, "Сутки — 400 рублей"),
        (1, "Пока что у нас так"),
        (2, "вы оформляете заказ на 8 мая"),
        (3, "Только начиная с завтрашнего дня"),
        (4, "Пока что нет"),
        (5, "Самокат приезжает к вам с полной зарядкой"),
        (6, "пока самокат не привезли"),
        (7, "Всем самокатов!")
    ])
    def test_click_pointer(self, driver, pointer_index, expected_text):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer(pointer_index)
        assert expected_text in main_page.get_text_under_pointer(pointer_index)
