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
