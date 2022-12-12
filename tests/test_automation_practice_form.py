from model.pages import automation_practice_form
from model.pages.automation_practice_form import form
from tests.tests_data.user import test_user


def test_submit_from():
    automation_practice_form.given_opened_wo_ads()

    automation_practice_form.fill_name(test_user.first_name, test_user.last_name)
    automation_practice_form.fill_email(test_user.email)
    automation_practice_form.fill_phone(test_user.phone)
    automation_practice_form.fill_birthday(test_user.birthday_day,
                                           test_user.birthday_month,
                                           test_user.birthday_year)
    # OR
    # automation_practice_form.fill_birthday2(test_user.birthday_day,
    #                                        test_user.birthday_month,
    #                                        test_user.birthday_year)
    automation_practice_form.choose_gender(test_user.gender.value)
    automation_practice_form.fill_subjects(test_user.subjects)
    automation_practice_form.check_hobby(test_user.hobbies)
    automation_practice_form.upload_picture(test_user.picture_path)
    automation_practice_form.fill_address(test_user.address)
    automation_practice_form.choose_state(test_user.state)
    automation_practice_form.choose_city(test_user.city)

    automation_practice_form.submit_form()
    automation_practice_form.validate_form(test_user, form)
