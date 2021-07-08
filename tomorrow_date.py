from datetime import datetime, timedelta
import freezegun


def get_tomorrow():
    presentday = datetime.now()

    tomorrow = presentday + timedelta(1)

    print("Today = ", presentday.strftime('%d-%m-%Y'))
    print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))
    return tomorrow.strftime('%d-%m-%Y')


def five_days_from_now():
    return datetime.now() + timedelta(days=5)


@freezegun.freeze_time("2020-05-15")
def test_five_days_from_now():
    assert five_days_from_now() == datetime.now() + timedelta(days=5)
