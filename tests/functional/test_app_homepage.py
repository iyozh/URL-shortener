import pytest
from selenium.webdriver.remote.webelement import WebElement

from tests.functional.pages import HomePage

url = "http://127.0.0.1:8000"


@pytest.mark.functional
def test_get(browser):
    page = HomePage(browser, url)

    validate_title(page)
    validate_structure(page)
    validate_content(page, "URL Shortener")


def validate_title(page: HomePage):
    assert "Homepage" in page.title


def validate_structure(page: HomePage):
    assert "form" in page.html

    button_shorten: WebElement = page.button_shorten
    assert button_shorten.tag_name == "button"

    input_link = page.input_link
    assert input_link.tag_name == "input"


def validate_content(page: HomePage, content):
    html = page.html
    assert content in html
