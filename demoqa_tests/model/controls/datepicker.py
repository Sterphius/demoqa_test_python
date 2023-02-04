import datetime
import sys
from selenium.webdriver import Keys

import selene

from demoqa_tests.utils import config


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, date: datetime.date):
        self.element.send_keys(
            Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a') \
            .type(date.strftime(config.input_datetime_format))
