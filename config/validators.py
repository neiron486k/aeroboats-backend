from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size: int = None):
        self.max_size = max_size * 1024 * 1024

    def __call__(self, file) -> None:
        if self.max_size and file.size > self.max_size:
            raise ValidationError(
                _("File size must be lower than %(limit)s.") % {"limit": filesizeformat(self.max_size)}
            )


def validate_full_name(value: str):
    import re

    message = _("Incorrect full name %(value)s.") % {"value": value}

    if not re.match("^[a-zA-zА-Яа-я ']+$", value):
        raise ValidationError(message)

    value = re.sub(" +", " ", value).strip()

    if len(value.split(" ")) < 2:
        raise ValidationError(message)
