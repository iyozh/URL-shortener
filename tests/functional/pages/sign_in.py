from selenium.webdriver.common.by import By

from tests.functional.pages import PageObject, PageElement


class SignInPage(PageObject):
    input_user = PageElement(By.CSS_SELECTOR, "input#id_username")
    input_password = PageElement(By.CSS_SELECTOR, "input#id_password")
    button_sign_in = PageElement(By.CSS_SELECTOR, "button#id_sign_in")
