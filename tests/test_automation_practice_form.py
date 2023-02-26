from demoqa_tests.model.pages.automation_practice_form import practice_form
from tests.tests_data.user import User
import allure


@allure.title("Successful fill automation practice form")
def test_submit_from():
    test_user = User(first_name='first', last_name='last')

    with allure.step("Open registrations form"):
        practice_form.given_opened_wo_ads()

    with allure.step("Fill form"):
        practice_form.fill_data(test_user).submit()

    with allure.step("Verify registration form"):
        practice_form.should_have_registered(test_user)
