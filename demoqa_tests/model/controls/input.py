import selene


class Input:
    def __init__(self, element: selene.Element):
        self.element = element

    def fill_text(self, value: str):
        self.element.should(selene.be.blank).type(value)

    def fill_texts_with_autocomplete(self, values: list[str]):
        for value in values:
            self.element.should(selene.be.blank).type(value).press_enter()
