import selene
from selene import have


class Radio:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, value: str):
        self.element.element_by(have.value(value)).element('..').click()
