import re
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.functional.pages import HomePage

url = "http://127.0.0.1:8000"


@pytest.mark.functional
def test_get(browser):
    page = HomePage(browser, url)

    validate_title(page)
    validate_structure(page)
    validate_content(page, "URL Shortener")


@pytest.mark.functional
def test_post(browser):

    link = "http://example.com"

    page = HomePage(browser, url)

    validate_title(page)
    validate_structure(page)
    validate_content(page, "URL Shortener")

    enter_link(page, link)
    submit(page)
    validate_redirect(page)
    validate_content(page, "URL Shortener")
    validate_structure(page)
    validate_result(page)

    submit(page)
    validate_redirect(page)
    validate_content(page, "Enter a valid URL")

    enter_link(page, "")
    submit(page)
    validate_redirect(page)
    validate_content(page, "Enter a valid URL")

    enter_link(page, "abc123")
    submit(page)
    validate_redirect(page)
    validate_content(page, "Enter a valid URL")


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


def enter_link(page: HomePage, link):
    page.input_link.clear()
    if link:
        page.input_link.send_keys(link)


def submit(page: HomePage):
    page.button_shorten.send_keys(Keys.RETURN)


def validate_redirect(page: HomePage):
    try:
        redirect = WebDriverWait(page.browser, 4).until(expected_conditions.url_matches(url))
        assert redirect
    except TimeoutException:
        raise AssertionError("no redirect")


def validate_result(page: HomePage):
    shortcut = page.input_link.get_attribute("value")
    assert re.match("http://127.0.0.1:8000/.{4}$", shortcut)
