
from selene.support.shared import browser
from selene import be, have


def test_google_not_find():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdlkfjasdf12345').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу asdlkfjasdf12345 ничего не найдено'))