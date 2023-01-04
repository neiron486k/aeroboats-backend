from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_file_size(file):
    limit = 2

    if file.size > limit * 1024 * 1024:
        raise ValidationError(_("File size must be lower than %(limit)d.") % {"limit": limit})


def validate_video_extension(value):
    import os

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ("mp4", "mov", "avi")

    if not ext.lower() in valid_extensions:
        raise ValidationError(_("Unsupported file extension."))


def validate_full_name(value: str):
    import re

    message = _("Incorrect full name %(value)s.") % {"value": value}

    if not re.match("^[a-zA-zА-Яа-я ']+$", value):
        raise ValidationError(message)

    value = re.sub(" +", " ", value).strip()

    if len(value.split(" ")) < 2:
        raise ValidationError(message)
