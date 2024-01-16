import allure
import pytest
from pages.order_page import OrderPage
from conftest import driver


@allure.story('Test create order')
class TestOrderPage:
    @allure.title('Test order from button in header')
    @pytest.mark.parametrize('name, surname, adress, number, comment',
                             [('Кристина', 'Наумова', 'Москва', '89177953313', 'ТЕСТ')])
    def test_create_oder_from_header_button_positive(self, driver, name, surname, adress, number, comment):
        order_page = OrderPage(driver)
        self.perform_order_from_header(order_page, name, surname, adress, number, comment)

    @allure.title('Test order from button in down page')
    @pytest.mark.parametrize('name, surname, adress, number, comment',
                             [('Тестер', 'Тестович', 'Москва', '15940505059', 'Проверка')])
    def test_create_oder_from_down_button_positive(self, driver, name, surname, adress, number, comment):
        order_page = OrderPage(driver)
        self.perform_order_from_down_page(order_page, name, surname, adress, number, comment)

    def perform_order_from_header(self, order_page, name, surname, adress, number, comment):
        order_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        order_page.click_button_cookie()
        order_page.click_order_button_from_header()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_adress(adress)
        order_page.enter_metro_filed()
        order_page.enter_phone_filed(number)
        order_page.click_next_button()
        order_page.enter_when_filed()
        order_page.enter_period_filed()
        order_page.click_on_checkbox_grey()
        order_page.enter_comment_filed(comment)
        order_page.click_order_button()
        order_page.click_yes_in_popup()
        # проверка всплывающего окна с сообщением об успешном создании заказа через кнопку 'Посмотреть статус'
        assert order_page.get_text_from_button_in_popup() == 'Посмотреть статус'

    def perform_order_from_down_page(self, order_page, name, surname, adress, number, comment):
        order_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        order_page.click_button_cookie()
        order_page.click_order_button_from_down_page()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_adress(adress)
        order_page.enter_metro_filed()
        order_page.enter_phone_filed(number)
        order_page.click_next_button()
        order_page.enter_when_filed()
        order_page.enter_period_filed()
        order_page.click_on_checkbox_grey()
        order_page.enter_comment_filed(comment)
        order_page.click_order_button()
        order_page.click_yes_in_popup()
        # проверка всплывающего окна с сообщением об успешном создании заказа через кнопку 'Посмотреть статус'
        assert order_page.get_text_from_button_in_popup() == 'Посмотреть статус'
