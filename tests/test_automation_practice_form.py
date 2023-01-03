from demoqa_tests.model.pages.automation_practice_form import practice_form
from tests.tests_data.user import User


def test_submit_from():
    test_user = User(first_name='first', last_name='last')
    practice_form.given_opened_wo_ads()

    practice_form.fill_data(test_user).submit()

    practice_form.should_have_registered(test_user)
