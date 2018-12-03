from marshmallow import ValidationError

from datetime import datetime


def check_future_date(value):
    if value < datetime.now().date():
        raise ValidationError("Please set date to a future date")


