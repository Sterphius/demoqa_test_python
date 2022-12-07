import os

from selene.support.shared import browser
from selene import command, have, be


def given_opened_page_wo_ads():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.all('[id^=google_ads_iframe][id$=__container__]') \
        .should(have.size_greater_than_or_equal(3)) \
        .perform(command.js.remove)


def test_submit_from():
    given_opened_page_wo_ads()

    browser.element('#firstName').should(be.blank).type('firstName')
    browser.element('#lastName').should(be.blank).type('lastName')
    browser.element('#userEmail').should(be.blank).type('name@example.com')

    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('#userNumber').should(be.blank).type('71234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('March')
    browser.element('.react-datepicker__year-select').send_keys('1990')
    browser.element(
        f'.react-datepicker__day--005'
        f':not(.react-datepicker__day--outside-month)'
    ).click()

    browser.element('#subjectsInput').should(be.blank).type('Physics').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'resources/sample.png')))

    browser.element('#currentAddress').should(be.blank).type('Sample address')
    browser.element('#react-select-3-input').perform(command.js.scroll_into_view).type('NCR').press_enter()
    browser.element('#react-select-4-input').perform(command.js.scroll_into_view).type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
    browser.element('.modal-content') \
        .all('tbody tr') \
        .all('td').should(
        have.texts(
            'Student Name', 'firstName lastName',
            'Student Email', 'name@example.com',
            'Gender', 'Male',
            'Mobile', '7123456789',
            'Date of Birth', '05 March,1990',
            'Subjects', 'Physics',
            'Hobbies', 'Music',
            'Picture', 'sample.png',
            'Address', 'Sample address',
            'State and City', 'NCR Delhi'
        )
    )
