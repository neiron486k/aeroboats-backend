from django.core.exceptions import ValidationError
import re


def file_size(file):
    limit = 2

    if file.size > limit * 1024 * 1024:
        raise ValidationError(f"File size must be lower than {limit}")


def full_name(value: str):
    if not re.match("^[a-zA-zА-Яа-я ']+$", value):
        raise ValidationError(f"Incorrect full name {value}")

    value = re.sub(" +", " ", value).strip()

    if len(value.split(" ")) < 2:
        raise ValidationError(f"Incorrect full name {value}")
