import pytest
from selene import browser
@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    yield
    browser.quit()