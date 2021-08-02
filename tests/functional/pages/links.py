from selenium.webdriver.common.by import By

from tests.functional.pages import PageObject, PageElement


class LinksPage(PageObject):
    div_links = PageElement(By.CSS_SELECTOR, "div#id_links_list")
    div_list_item = PageElement(By.CSS_SELECTOR, "div#id_list_item")