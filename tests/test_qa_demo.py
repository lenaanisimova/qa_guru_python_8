from selene import browser, have, be
import os

def test_full_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Anisimova')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element(('css selector', 'label[for="gender-radio-2"]')).click()
    browser.element('#userNumber').type('7912345678')
    #Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element('.react-datepicker__day--002').click()

    browser.element('#subjectsInput').type('History').press_enter()
    browser.element(('css selector', 'label[for="hobbies-checkbox-2"]')).click()

    #browser.element("#uploadPicture").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/iris.jpeg'))

    browser.element("#currentAddress").type('Volgograd')

    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()
    #Проверка перед отправкой
    #browser.element('.modal-content').should(be.visible)
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
    #browser.all("tbody tr td:last-child").should(have.exact_texts(
        'Elena Anisimova',
        'test@gmail.com',
        'Female',
        '7912345678',
        '02 October,1990',
        'History',
        'Reading',
        'iris.jpeg',
        'Volgograd',
        'NCR Noida'))


