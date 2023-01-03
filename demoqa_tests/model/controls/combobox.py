import selene


class ComboBox:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, value: str):
        self.element.perform(selene.command.js.scroll_into_view) \
            .type(value). \
            press_enter()
