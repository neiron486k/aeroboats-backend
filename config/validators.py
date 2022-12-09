from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext as _


def file_size(file):
    limit = 2

    if file.size > limit * 1024 * 1024:
        raise ValidationError(_("File size must be lower than %(limit)d.") % {'limit': limit})


def full_name(value: str):
    message = _("Incorrect full name %(value)s.") % {'value': value}

    if not re.match("^[a-zA-zА-Яа-я ']+$", value):
        raise ValidationError(message)

    value = re.sub(" +", " ", value).strip()

    if len(value.split(" ")) < 2:
        raise ValidationError(message)
