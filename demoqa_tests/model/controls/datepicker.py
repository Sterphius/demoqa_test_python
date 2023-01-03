import datetime
import sys
from selenium.webdriver import Keys

import selene

import demoqa_tests.utils.config


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, value: datetime.date):
        if sys.platform == 'darwin':
            key = Keys.COMMAND
        else:
            key = Keys.CONTROL
        self.element.send_keys(key, 'a').type(value.strftime(demoqa_tests.utils.config.input_datetime_format)) \
            .press_enter()
