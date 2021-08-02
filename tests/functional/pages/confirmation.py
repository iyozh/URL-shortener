from selenium.webdriver.common.by import By

from tests.functional.pages import PageObject, PageElement


class ConfirmationPage(PageObject):
    button_yes = PageElement(By.CSS_SELECTOR, "button#id_yes")