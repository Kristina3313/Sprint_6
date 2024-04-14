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

    @allure.step('Клик на кнопку с принятием куки')
    def click_button_cookie(self):
        self.find_and_click_element(self.button_cookie)

    @allure.step('Клик на кнопку "Заказать" в хэдере')
    def click_order_button_from_header(self):
        self.find_and_click_element(self.buttonOrderHeader)

    @allure.step('Клик на кнопку "Заказать" в нижней части страницы')
    def click_order_button_from_down_page(self):
        self.find_and_click_element(self.buttonOrderDownPage)

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.input_text(self.inputName, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.input_text(self.inputFamiliya, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.input_text(self.inputAdress, address)

    @allure.step('Выбор метро')
    def select_metro(self):
        self.choose_option_from_dropdown(self.chooseMetro, self.metroPreobrazhenskaya)

    @allure.step('Ввод номера телефона')
    def enter_phone_field(self, number):
        self.input_text(self.inputNumber, number)

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.find_and_click_element(self.buttonNext)

    @allure.step('Выбор дня')
    def select_date(self):
        self.choose_option_from_dropdown(self.inputWhere, self.choose31january)

    @allure.step('Выбор периода')
    def select_period(self):
        self.choose_option_from_dropdown(self.inputPeriod, self.choose2days)

    @allure.step('Клик на чек-бокс "Серый"')
    def click_on_grey_checkbox(self):
        self.find_and_click_element(self.checkBoxGrey)

    @allure.step('Ввод комментария')
    def enter_comment_field(self, comment):
        self.input_text(self.inputComment, comment)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.find_and_click_element(self.buttonZakazat)

    @allure.step('Клик на кнопку "Да" в поп-апе')
    def click_yes_in_popup(self):
        self.find_and_click_element(self.buttonYes)

    @allure.step('Получение текста из кнопки')
    def get_text_from_button_in_popup(self):
        return self.get_text_from_element(self.button_check_status)
