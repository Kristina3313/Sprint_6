from selenium.webdriver.common.by import By


class LocatorsMain:
    # Селектор стрелки "Сколько это стоит? И как оплатить?"
    POINTER0 = (By.XPATH, "//div[@id='accordion__heading-0']")
    # Селектор стрелки "Хочу сразу несколько самокатов! Так можно?"
    POINTER1 = (By.XPATH, "// div[ @ id = 'accordion__heading-1']")
    # Селектор стрелки "Как рассчитывается время аренды?"
    POINTER2 = (By.XPATH, "//div[@id='accordion__heading-2']")
    # Селектор стрелки "Можно ли заказать самокат прямо на сегодня?"
    POINTER3 = (By.XPATH, "//div[@id='accordion__heading-3']")
    # Селектор стрелки "Можно ли продлить заказ или вернуть самокат раньше?"
    POINTER4 = (By.XPATH, "//div[@id='accordion__heading-4']")
    # Селектор стрелки "Вы привозите зарядку вместе с самокатом?"
    POINTER5 = (By.XPATH, "//div[@id='accordion__heading-5']")
    # Селектор стрелки "Можно ли отменить заказ?"
    POINTER6 = (By.XPATH, "//div[@id='accordion__heading-6']")
    # Селектор стрелки "Я живу за МКАДом, привезёте?"
    POINTER7 = (By.XPATH, "//div[@id='accordion__heading-7']")
    # Кнопка "Статус заказа"
    BUTTON_CHECK_STATUS = (By.XPATH, "//button[contains(text(),'Статус заказа')]")
    # Кнопка принять печеньки
    BUTTON_COOKIE = (By.ID, "rcc-confirm-button")
    # лого Самокат
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    # Лого Яндекс
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    # кнопка "Заказать" в хэдере
    BUTTON_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(), 'Заказать')]")
    # кнопка "Заказать" в нижней части страницы
    BUTTON_DOWNPAGE = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    # текст под указателем 0
    TEXT_UNDER_POINTER0 = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]")
    # текст под указателем 1
    TEXT_UNDER_POINTER1 = (By.XPATH,"//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]")
    # текст под указателем 2
    TEXT_UNDER_POINTER2 = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]")
    # текст под указателем 3
    TEXT_UNDER_POINTER3 = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]")
    # текст под указателем 4
    TEXT_UNDER_POINTER4 = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]")
    # текст под указателем 5
    TEXT_UNDER_POINTER5 = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]")
    # текст под указателем 6
    TEXT_UNDER_POINTER6 = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]")
    # текст под указателем 7
    TEXT_UNDER_POINTER7 = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]")
