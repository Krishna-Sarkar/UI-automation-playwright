import pytest
from playwright.sync_api import Page, Browser, BrowserContext, Playwright

@pytest.fixture()
def setup_teardown(page:Page):
    page.set_default_timeout(120000)
    yield page
