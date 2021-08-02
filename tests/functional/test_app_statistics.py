import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import LinksPage, ConfirmationPage
from tests.functional.pages import LinksSettingsPage

url = 'http://127.0.0.1:8000/statistics/'


@pytest.mark.functional
def test_get_links(browser):
    page = LinksPage(browser, url)

    validate_title(page, "Links")
    validate_structure(page)
    validate_content(page, "URL Shortener", "My links")

    click_link(page, "id_more")
    validate_title(page, 'Statistics')
    validate_content(page, 'Total clicks', 'Settings', 'IP', 'Location')


def test_get_statistics(browser):
    current_url = browser.current_url
    page = LinksSettingsPage(browser, current_url)

    validate_title(page, "Statistics")
    validate_statistics_structure(page)
    validate_content(page, 'Total clicks', 'Settings', 'IP', 'Location')


def test_post(browser):
    current_url = browser.current_url
    page = LinksSettingsPage(browser, current_url)

    validate_title(page, "Statistics")
    validate_statistics_structure(page)
    validate_content(page, 'Total clicks', 'Settings', 'IP', 'Location')

    fill_checkbox(page)
    submit_confirmation(page)
    validate_redirect(page, current_url)
    validate_title(page, "Statistics")
    validate_checkbox(page)
    validate_statistics_structure(page)
    validate_content(page, 'Total clicks', 'Settings', 'IP', 'Location')

    set_utm_source(page, 'google')
    set_utm_medium(page, 'cpc')
    set_utm_campaign(page, 'promo')
    set_utm_term(page, 'link')
    set_utm_content(page, 'free')
    submit_utm(page)
    validate_redirect(page, current_url)
    validate_title(page, "Statistics")
    validate_statistics_structure(page)
    validate_content(page, 'Total clicks', 'Settings', 'IP', 'Location')

    click_link(page, "id_shortcut")
    validate_title(page, "Confirmation")
    validate_content(page, 'Confirmation Page')


def test_confirmation(browser):
    current_url = browser.current_url
    page = ConfirmationPage(browser, current_url)

    validate_title(page, "Confirmation")
    validate_confirmation_structure(page)
    validate_content(page, "Confirmation Page")


def validate_title(page, title):
    assert title in page.title


def validate_structure(page: LinksPage):
    assert "links-list" in page.html

    div_links_list = page.div_links
    assert div_links_list.tag_name == 'div'

    div_link = page.div_list_item
    assert div_link.tag_name == 'div'


def validate_content(page, *content):
    html = page.html
    for text in content:
        assert text in html


def validate_checkbox(page: LinksSettingsPage):
    assert page.input_confirm.get_attribute('checked')


def click_link(page, element_id):
    sign_out = page.browser.find_element_by_id(element_id)
    sign_out.click()


def validate_statistics_structure(page: LinksSettingsPage):
    assert "form" in page.html

    input_confirm = page.input_confirm
    assert input_confirm.tag_name == "input"

    input_source = page.input_utm_source
    assert input_source.tag_name == "input"

    input_utm_medium = page.input_utm_medium
    assert input_utm_medium.tag_name == "input"

    input_utm_campaign = page.input_utm_campaign
    assert input_utm_campaign.tag_name == "input"

    input_utm_term = page.input_utm_term
    assert input_utm_term.tag_name == "input"

    input_utm_content = page.input_utm_content
    assert input_utm_content.tag_name == "input"

    button_confirm = page.button_confirm
    assert button_confirm.tag_name == "button"

    button_utm = page.button_utm
    assert button_utm.tag_name == "button"

    button_delete = page.button_delete
    assert button_delete.tag_name == "button"


def fill_checkbox(page: LinksSettingsPage):
    page.input_confirm.click()


def submit_confirmation(page: LinksSettingsPage):
    page.button_confirm.send_keys(Keys.RETURN)


def validate_redirect(page, redirect_url):
    try:
        redirect = WebDriverWait(page.browser, 4).until(expected_conditions.url_matches(redirect_url))
        assert redirect
    except TimeoutException:
        raise AssertionError("no redirect")


def set_utm_source(page: LinksSettingsPage, value):
    page.input_utm_source.clear()
    if value:
        page.input_utm_source.send_keys(value)


def set_utm_medium(page: LinksSettingsPage, value):
    page.input_utm_medium.clear()
    if value:
        page.input_utm_medium.send_keys(value)


def set_utm_campaign(page: LinksSettingsPage, value):
    page.input_utm_campaign.clear()
    if value:
        page.input_utm_campaign.send_keys(value)


def set_utm_term(page: LinksSettingsPage, value):
    page.input_utm_term.clear()
    if value:
        page.input_utm_term.send_keys(value)


def set_utm_content(page: LinksSettingsPage, value):
    page.input_utm_content.clear()
    if value:
        page.input_utm_content.send_keys(value)


def submit_utm(page: LinksSettingsPage):
    page.button_utm.send_keys(Keys.RETURN)


def validate_confirmation_structure(page: ConfirmationPage):
    assert 'button' in page.html

    button_yes = page.button_yes
    assert button_yes.tag_name == 'button'
