from typing import Union

from selenium.webdriver.android.webdriver import WebDriver as AndroidWebDriver
from selenium.webdriver.blackberry.webdriver import WebDriver as BlackberryWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IeWebDriver
from selenium.webdriver.opera.webdriver import WebDriver as OperaWebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver as PhantomJsWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.safari.webdriver import WebDriver as SafariWebDriver

WebDriverT = Union[
    AndroidWebDriver,
    BlackberryWebDriver,
    ChromeWebDriver,
    EdgeWebDriver,
    FirefoxWebDriver,
    IeWebDriver,
    OperaWebDriver,
    PhantomJsWebDriver,
    RemoteWebDriver,
    SafariWebDriver,
]


class PageObject:
    def __init__(self, browser: WebDriverT, url: str):
        self._browser = browser
        self._url = url
        self._browser.get(f"{self._url}")

    @property
    def browser(self):
        return self._browser

    @property
    def html(self) -> str:
        return self.browser.page_source

    @property
    def title(self) -> str:
        return self.browser.title


class PageElement:
    def __init__(self, by, value):
        self._by = by
        self._value = value

    def __get__(self, page_object: PageObject, page_object_cls: type):
        if not page_object:
            return self

        return page_object.browser.find_element(self._by, self._value)
