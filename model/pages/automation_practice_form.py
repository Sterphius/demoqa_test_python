import os
import sys
from pathlib import Path
from typing import Tuple

from selenium.webdriver import Keys

from selene.support.shared import browser
from selene import command, have, be

import resources
from tests.tests_data import user
from tests.tests_data.user import User


def given_opened_wo_ads():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads_iframe][id$=__container__]') \
        .should(have.size_greater_than_or_equal(0)) \
        .perform(command.js.remove)


def fill_name(firstname: str, lastname: str):
    browser.element('#firstName').should(be.blank).type(firstname)
    browser.element('#lastName').should(be.blank).type(lastname)


def fill_email(email: str):
    browser.element('#userEmail').should(be.blank).type(email)


def fill_phone(phone: str):
    browser.element('#userNumber').should(be.blank).type(phone)


def check_hobby(hobbies: Tuple[user.Hobbies]):
    for item in hobbies:
        browser.element(f'[for=hobbies-checkbox-{item.value}]').click()


def fill_birthday(day, month, year: str):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()


def fill_birthday2(day, month, year: str):
    if sys.platform == 'darwin':
        key = Keys.COMMAND
    else:
        key = Keys.CONTROL
    browser.element('#dateOfBirthInput').send_keys(key, 'a').type(f'{day} {month} {year}').press_enter()


def fill_subjects(subjects: Tuple[str]):
    for subject in subjects:
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()


def choose_gender(gender: user.Gender):
    browser.element(f'[id^=gender-radio][value={gender}').perform(command.js.click)


def upload_picture(relative_path: str):
    browser.element('#uploadPicture').send_keys(
        str(Path(resources.__file__).parent.joinpath(relative_path).absolute()))


def fill_address(address: str):
    browser.element('#currentAddress').should(be.blank).type(address)


def choose_state(state: str):
    browser.element('#react-select-3-input').perform(command.js.scroll_into_view).type(state).press_enter()


def choose_city(city: str):
    browser.element('#react-select-4-input').perform(command.js.scroll_into_view).type(city).press_enter()


def submit_form():
    browser.element('#submit').press_enter()


class PracticeForm:
    studentName = 'Student Name'
    studentEmail = 'Student Email'
    gender = 'Gender'
    mobile = 'Mobile'
    birthDate = 'Date of Birth'
    subjects = 'Subjects'
    hobbies = 'Hobbies'
    picture = 'Picture'
    address = 'Address'
    stateAndCity = 'State and City'


def string_from_tuple_of_enums(item: Tuple):
    string = item[0].name
    for i in range(0, len(item) - 1):
        string = string + ', ' + item[i + 1].name
    return string


def validate_form(user_data: User, practice_form: PracticeForm):
    browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
    browser.element('.modal-content') \
        .all('tbody tr') \
        .all('td').should(
        have.texts(
            practice_form.studentName, f'{user_data.first_name} {user_data.last_name}',
            practice_form.studentEmail, user_data.email,
            practice_form.gender, user_data.gender.value,
            practice_form.mobile, user_data.phone,
            practice_form.birthDate, f'{user_data.birthday_day} {user_data.birthday_month},{user_data.birthday_year}',
            practice_form.subjects, ', '.join(user_data.subjects),
            practice_form.hobbies, string_from_tuple_of_enums(user_data.hobbies),
            practice_form.picture, os.path.split(user_data.picture_path)[-1],
            practice_form.address, user_data.address,
            practice_form.stateAndCity, f'{user_data.state} {user_data.city}'
        )
    )


form = PracticeForm()
