import allure
from conftest import driver
from pages.dzen_page import DzenPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.story('Тест элементов на главной странице')
class TestMainPage:
    @allure.title("Тест проверки отображения текста под стрелкой 0")
    def test_click_pointer0(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer0()
        assert "Сутки — 400 рублей" in main_page.get_text_under_pointer0()

    @allure.title("Тест проверки отображения текста под стрелкой 1")
    def test_click_pointer1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer1()
        assert "Пока что у нас так" in main_page.get_text_under_pointer1()

    @allure.title("Тест проверки отображения текста под стрелкой 2")
    def test_click_pointer2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer2()
        assert "вы оформляете заказ на 8 мая" in main_page.get_text_under_pointer2()

    @allure.title("Тест проверки отображения текста под стрелкой 3")
    def test_click_pointer3(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer3()
        assert "Только начиная с завтрашнего дня" in main_page.get_text_under_pointer3()

    @allure.title("Тест проверки отображения текста под стрелкой 4")
    def test_click_pointer4(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer4()
        assert "Пока что нет" in main_page.get_text_under_pointer4()

    @allure.title("Тест проверки отображения текста под стрелкой 5")
    def test_click_pointer5(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer5()
        assert "Самокат приезжает к вам с полной зарядкой" in main_page.get_text_under_pointer5()

    @allure.title("Тест проверки отображения текста под стрелкой 6")
    def test_click_pointer6(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer6()
        assert "пока самокат не привезли" in main_page.get_text_under_pointer6()

    @allure.title("Тест проверки отображения текста под стрелкой 7")
    def test_click_pointer7(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer7()
        assert "Всем самокатов!" in main_page.get_text_under_pointer7()

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
