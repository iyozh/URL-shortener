import secrets

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import SignUpPage, SignInPage

sign_up_url = 'http://127.0.0.1:8000/onboarding/sign-up/'
homepage_url = 'http://127.0.0.1:8000'
sign_out_url = 'http://127.0.0.1:8000/onboarding/sign-out/'
sign_in_url = 'http://127.0.0.1:8000/onboarding/sign-in/'

username = secrets.token_hex(5)
password = secrets.token_hex(5)


@pytest.mark.functional
def test_get_sign_up(browser):
    page = SignUpPage(browser, sign_up_url)

    validate_title(page, 'Sign Up')
    validate_structure(page)
    validate_content(page, "Sign Up")


@pytest.mark.functional
def test_registration(browser):
    page = SignUpPage(browser, sign_up_url)

    email = 'example@gmail.com'
    location = "BY"
    birth_date = "2020-08-29"

    validate_title(page, 'Sign Up')
    validate_structure(page)
    validate_content(page, "Sign Up")

    enter_username(page, username)
    enter_password(page, password)
    enter_password_confirm(page, password)
    enter_email(page, email)
    select_location(page, location)
    enter_birth_date(page, birth_date)
    submit(page)
    validate_redirect(page, homepage_url)
    validate_content(page, username)

    click_link(page, 'sign-out')
    validate_redirect(page, sign_out_url)
    validate_content(page, 'You have been signed out')


@pytest.mark.functional
def test_get_sign_in(browser):
    page = SignInPage(browser, sign_in_url)

    validate_title(page, 'Sign In')
    validate_sign_in_structure(page)
    validate_content(page, "Sign In")


@pytest.mark.functional
def test_login(browser):
    page = SignInPage(browser, sign_in_url)

    validate_title(page, 'Sign In')
    validate_sign_in_structure(page)
    validate_content(page, "Sign In")

    enter_username(page, username)
    enter_password(page, password)
    submit_login(page)
    validate_redirect(page, homepage_url)
    validate_content(page, username)


def validate_title(page, title):
    assert title in page.title


def validate_sign_in_structure(page: SignInPage):
    assert 'form' in page.html

    input_user = page.input_user
    assert input_user.tag_name == "input"

    input_password = page.input_password
    assert input_password.tag_name == "input"

    button_sign_in = page.button_sign_in
    assert button_sign_in.tag_name == "button"


def validate_structure(page: SignUpPage):
    assert "form" in page.html

    input_user = page.input_user
    assert input_user.tag_name == "input"

    input_password = page.input_password
    assert input_password.tag_name == "input"

    input_password_confirm = page.input_password_confirm
    assert input_password_confirm.tag_name == "input"

    select = page.select_location
    assert select.tag_name == "select"

    input_birth_date = page.input_birth_date
    assert input_birth_date.tag_name == "input"

    button_sign_up: WebElement = page.button_sign_up
    assert button_sign_up.tag_name == "button"


def validate_content(page, content):
    html = page.html
    assert content in html


def enter_username(page, user):
    page.input_user.clear()
    if username:
        page.input_user.send_keys(user)


def enter_email(page: SignUpPage, email):
    page.input_email.clear()
    if email:
        page.input_email.send_keys(email)


def enter_password(page, password):
    page.input_password.clear()
    if password:
        page.input_password.send_keys(password)


def enter_password_confirm(page: SignUpPage, password):
    page.input_password_confirm.clear()
    if password:
        page.input_password_confirm.send_keys(password)


def select_location(page: SignUpPage, value):
    select = Select(page.select_location)
    select.select_by_value(value)


def enter_birth_date(page: SignUpPage, birth_date):
    page.input_birth_date.clear()
    if birth_date:
        page.input_birth_date.send_keys(birth_date)


def submit(page: SignUpPage):
    page.button_sign_up.send_keys(Keys.RETURN)


def validate_redirect(page, redirect_url):
    try:
        redirect = WebDriverWait(page.browser, 4).until(expected_conditions.url_matches(redirect_url))
        assert redirect
    except TimeoutException:
        raise AssertionError("no redirect")


def click_link(page: SignUpPage, element_id):
    sign_out = page.browser.find_element_by_id(element_id)
    sign_out.click()


def submit_login(page: SignInPage):
    page.button_sign_in.send_keys(Keys.RETURN)
