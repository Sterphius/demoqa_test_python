from pathlib import Path

import selene

import resources


class Upload:
    def __init__(self, element: selene.Element):
        self.element = element

    def file_from_resources(self, value: str):
        self.element.send_keys(
            str(Path(resources.__file__)
                .parent
                .joinpath(value)
                .absolute()))
