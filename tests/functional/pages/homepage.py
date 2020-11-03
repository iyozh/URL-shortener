from selenium.webdriver.common.by import By

from .abstract import PageObject
from .abstract import PageElement


class HomePage(PageObject):
    input_link = PageElement(By.CSS_SELECTOR, "input#id_original")
    button_shorten = PageElement(By.CSS_SELECTOR, "button#shorten-button-id")
