import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import LocatorsDzen


class DzenPage(BasePage):
    CARD_NEWS = LocatorsDzen.CARD_NEWS

    @allure.step("Get element from dzen page")
    def get_elements_news(self):
        all_elements = self.find_elements_located(DzenPage.CARD_NEWS)
        text_fom_card = [element.text for element in all_elements]
        return text_fom_card
