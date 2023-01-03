from selene import have, command
from selene.support.shared import browser

ads = browser.all('[id^=google_ads_iframe][id$=__container__]')


def remove_ads(count: int):
    ads \
        .should(have.size_greater_than_or_equal(count)) \
        .perform(command.js.remove)
