from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.main_page_locators import LocatorsMain
from pages.base_page import BasePage
from locators.order_page_locators import LocatorsOrder


class OrderPage(BasePage):
    buttonOrderHeader = LocatorsMain.BUTTON_HEADER
    buttonOrderDownPage = LocatorsMain.BUTTON_DOWNPAGE
    inputName = LocatorsOrder.INPUT_NAME
    inputFamiliya = LocatorsOrder.INPUT_SURNAME
    inputAdress = LocatorsOrder.INPUT_ADRESS
    chooseMetro = LocatorsOrder.CHOOSE_METRO
    inputNumber = LocatorsOrder.INPUT_NUMBER
    buttonNext = LocatorsOrder.BUTTON_NEXT
    inputWhere = LocatorsOrder.INPUT_WHERE
    chooseCalendar = LocatorsOrder.CHOOSE_CALENDAR
    inputPeriod = LocatorsOrder.INPUT_PERIOD
    choosePeriod = LocatorsOrder.CHOOSE_3_DAYS
    checkBoxGrey = LocatorsOrder.GREY_CHECK_BOX
    inputComment = LocatorsOrder.INPUT_COMMENT
    buttonBack = LocatorsOrder.BUTTON_BACK
    buttonZakazat = LocatorsOrder.BUTTON_ZAKAZAT
    buttonYes = LocatorsOrder.BUTTON_YES
    button_check_status = LocatorsOrder.BUTTON_CHECK_STATUS
    button_cookie = LocatorsMain.BUTTON_COOKIE
    metroPreobrazhenskaya = LocatorsOrder.METRO_PREOBRAZHENSKAYA
    choose31january = LocatorsOrder.CHOOSE_31_JANUARY
    choose2days = LocatorsOrder.CHOOSE_2_DAYS

    # метод кликает на кнопку при открытии страницы "Да все привыкли"
    @allure.step('Click to button with cookie')
    def click_button_cookie(self):
        self.find_and_click_element(self.button_cookie)

    # метод кликает по кнопке "Заказать" в хэдере
    @allure.step('Click to button from header')
    def click_order_button_from_header(self):
        self.find_and_click_element(self.buttonOrderHeader)

    # метод кликает по кнопке "Заказать" в нижней части страницы
    @allure.step('Click to button from down page')
    def click_order_button_from_down_page(self):
        self.find_and_click_element(self.buttonOrderDownPage)

    @allure.step('Enter name')
    def input_name(self, name):
        self.input_text(self.inputName, name)

    @allure.step('Enter surname')
    def input_surname(self, surname):
        self.input_text(self.inputFamiliya, surname)

    @allure.step('Enter adress')
    def input_adress(self, adress):
        self.input_text(self.inputAdress, adress)

    @allure.step('Choose metro')
    def enter_metro_filed(self):
        self.choose_option_from_dropdown(self.chooseMetro, self.metroPreobrazhenskaya)

    @allure.step('Enter number phone')
    def enter_phone_filed(self, number):
        self.input_text(self.inputNumber, number)

    @allure.step('Click to button Next')
    def click_next_button(self):
        self.find_and_click_element(self.buttonNext)

    @allure.step('Choose day')
    def enter_when_filed(self):
        self.choose_option_from_dropdown(self.inputWhere, self.choose31january)

    @allure.step('Choose period')
    def enter_period_filed(self):
        self.choose_option_from_dropdown(self.inputPeriod, self.choose2days)

    @allure.step('Click to grey check-box')
    def click_on_checkbox_grey(self):
        self.find_and_click_element(self.checkBoxGrey)

    @allure.step('Enter comment')
    def enter_comment_filed(self, comment):
        self.input_text(self.inputComment, comment)

    @allure.step('Click to Zakazat button')
    def click_order_button(self):
        self.find_and_click_element(self.buttonZakazat)

    @allure.step('Click to Yes button in popup')
    def click_yes_in_popup(self):
        self.find_and_click_element(self.buttonYes)

    @allure.step('Get text from button')
    def get_text_from_button_in_popup(self):
        return self.driver.find_element(*self.button_check_status).text
