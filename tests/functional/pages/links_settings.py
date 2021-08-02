from selenium.webdriver.common.by import By

from tests.functional.pages import PageObject, PageElement


class LinksSettingsPage(PageObject):
    input_confirm = PageElement(By.CSS_SELECTOR, "input#id_confirm")
    button_confirm = PageElement(By.CSS_SELECTOR, "button#id_button_confirm")
    input_utm_source = PageElement(By.CSS_SELECTOR, "input#id_utm_source")
    input_utm_medium = PageElement(By.CSS_SELECTOR, "input#id_utm_medium")
    input_utm_campaign = PageElement(By.CSS_SELECTOR, "input#id_utm_campaign")
    input_utm_term = PageElement(By.CSS_SELECTOR, "input#id_utm_source")
    input_utm_content = PageElement(By.CSS_SELECTOR, "input#id_utm_content")
    button_utm = PageElement(By.CSS_SELECTOR, "button#id_button_utm")
    button_delete = PageElement(By.CSS_SELECTOR, "button#id_delete")
