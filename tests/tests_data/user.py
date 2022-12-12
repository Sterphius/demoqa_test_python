from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobbies(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclass
class User:
    gender: Gender = Gender.Male
    hobbies: Tuple[Hobbies] = (Hobbies.Sports, Hobbies.Reading)
    subjects: Tuple[str] = ('Physics', 'Math')
    birthday_day = '15'
    birthday_month = 'March'
    birthday_year = '1990'
    first_name: str = 'firstName'
    last_name: str = 'lastName'
    email: str = 'name@example.com'
    phone: str = '7123456789'
    picture_path: str = 'sample.png'
    address: str = 'Sample address'
    state: str = 'NCR'
    city: str = 'Delhi'


test_user = User()
