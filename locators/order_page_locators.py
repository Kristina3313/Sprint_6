from selenium.webdriver.common.by import By


class LocatorsOrder:
    # поле "Имя"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    # поле "Фамилия"
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # поле "Адрес"
    INPUT_ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле "Станция метро"
    CHOOSE_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Выбор станции в выпадающем списке
    METRO_PREOBRAZHENSKAYA = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Преображенская площадь']")
    # поле "Телефон"
    INPUT_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")
    # поле "Когда привезти"
    INPUT_WHERE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # выбор даты в календаре
    CHOOSE_CALENDAR = (By.XPATH, "//div[contains(text(),'31')]")
    # дата 31 января в календаре
    CHOOSE_31_JANUARY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--031') and text()='31']")
    # поле "Срок аренды"
    INPUT_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    # выбор периода в выпадающем списке
    CHOOSE_2_DAYS = (By.XPATH, "//div[contains(text(),'двое суток')]")
    #  выбор из выпадающего списка
    CHOOSE_3_DAYS = (By.XPATH, "//div[contains(text(),'трое суток')]")
    # Чек-бокс "Серая безысходность"
    GREY_CHECK_BOX = (By.XPATH, "//input[@id='grey']")
    # Поле "Комментарий для курьера"
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Назад"
    BUTTON_BACK = (By.XPATH, "//button[contains(text(),'Назад')]")
    # Кнопка "Заказать"
    BUTTON_ZAKAZAT = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    # Кнопка "Да" в поп-апе "Хотите оформить заказ?"
    BUTTON_YES = (By.XPATH, "//button[contains(text(),'Да')]")
    # кнопка "Посмотреть статус"
    BUTTON_CHECK_STATUS = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
