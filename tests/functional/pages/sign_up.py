from selenium.webdriver.common.by import By

from tests.functional.pages import PageObject, PageElement


class SignUpPage(PageObject):
    input_user = PageElement(By.CSS_SELECTOR, "input#id_username")
    input_email = PageElement(By.CSS_SELECTOR, "input#id_email")
    input_password = PageElement(By.CSS_SELECTOR, "input#id_password1")
    input_password_confirm = PageElement(By.CSS_SELECTOR, "input#id_password2")
    select_location = PageElement(By.CSS_SELECTOR, "select#id_location")
    input_birth_date = PageElement(By.CSS_SELECTOR, "input#id_birth_date")
    button_sign_up = PageElement(By.CSS_SELECTOR, "button#id_sign_up")