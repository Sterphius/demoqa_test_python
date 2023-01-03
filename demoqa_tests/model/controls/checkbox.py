import selene
from selene import have


class CheckBox:
    def __init__(self, element: selene.Element):
        self.element = element

    def activate_ids(self, values: tuple):
        for item in values:
            self.element.element_by(have.exact_text(item.name)).click()
