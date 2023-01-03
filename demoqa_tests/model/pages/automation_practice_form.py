import os
import datetime
from typing import Tuple

from selene.support.shared import browser
from selene import have, be

import demoqa_tests.utils.config
from demoqa_tests import utils
from demoqa_tests.model.controls.checkbox import CheckBox
from demoqa_tests.model.controls.combobox import ComboBox
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.input import Input
from demoqa_tests.model.controls.radio import Radio
from demoqa_tests.model.controls.upload import Upload
from demoqa_tests.model.third_party import google
from tests.tests_data.user import User


def string_from_tuple_of_enums(item: Tuple):
    string = item[0].name
    for i in range(0, len(item) - 1):
        string = string + ', ' + item[i + 1].name
    return string


class PracticeForm:
    def __init__(self):
        self.user = None

        self.studentName = 'Student Name'
        self.studentEmail = 'Student Email'
        self.gender = 'Gender'
        self.mobile = 'Mobile'
        self.birthDate = 'Date of Birth'
        self.subjects = 'Subjects'
        self.hobbies = 'Hobbies'
        self.picture = 'Picture'
        self.address = 'Address'
        self.stateAndCity = 'State and City'

    def given_opened_wo_ads(self):
        browser.open('/automation-practice-form')
        google.remove_ads(0)
        return self

    def fill_name(self):
        Input(browser.element('#firstName')).fill_text(self.user.first_name)
        Input(browser.element('#lastName')).fill_text(self.user.last_name)
        return self

    def fill_email(self):
        Input(browser.element('#userEmail')).fill_text(self.user.email)
        return self

    def fill_phone(self):
        Input(browser.element('#userNumber')).fill_text(self.user.phone)
        return self

    def check_hobby(self):
        CheckBox(browser.all('[for^=hobbies-checkbox]')).activate_ids(self.user.hobbies)
        return self

    def fill_birthday(self):
        DatePicker(browser.element('#dateOfBirthInput')) \
            .set_date(datetime.date(self.user.birthday_year, self.user.birthday_month, self.user.birthday_day))
        return self

    def fill_subjects(self):
        Input(browser.element('#subjectsInput')).fill_texts_with_autocomplete(self.user.subjects)
        return self

    def choose_gender(self):
        Radio(browser.all('[name=gender]')).select(self.user.gender.value)
        return self

    def upload_picture(self):
        Upload(browser.element('#uploadPicture')).file_from_resources(self.user.picture_path)
        return self

    def fill_address(self):
        Input(browser.element('#currentAddress')).fill_text(self.user.address)
        return self

    def choose_state(self):
        ComboBox(browser.element('#react-select-3-input')).select(self.user.state)
        return self

    def choose_city(self):
        ComboBox(browser.element('#react-select-4-input')).select(self.user.city)
        return self

    def submit_form(self):
        browser.element('#submit').press_enter()
        return self

    def should_have_registered(self, data: User):
        self.user = data
        browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
        browser.element('.modal-content') \
            .all('tbody tr') \
            .all('td').should(
            have.texts(
                self.studentName, f'{self.user.first_name} {self.user.last_name}',
                self.studentEmail, self.user.email,
                self.gender, self.user.gender.value,
                self.mobile, self.user.phone,
                self.birthDate,
                datetime.date(self.user.birthday_year, self.user.birthday_month, self.user.birthday_day)
                .strftime(utils.config.visible_datetime_format),
                self.subjects, ', '.join(self.user.subjects),
                self.hobbies, string_from_tuple_of_enums(self.user.hobbies),
                self.picture, os.path.split(self.user.picture_path)[-1],
                self.address, self.user.address,
                self.stateAndCity, f'{self.user.state} {self.user.city}'
            )
        )
        return self

    def fill_data(self, data: User):
        self.user = data

        self.fill_name() \
            .fill_email() \
            .fill_phone() \
            .fill_birthday() \
            .choose_gender() \
            .fill_subjects() \
            .check_hobby() \
            .upload_picture() \
            .fill_address() \
            .choose_state() \
            .choose_city()
        return self

    def submit(self):
        self.submit_form()


practice_form = PracticeForm()
