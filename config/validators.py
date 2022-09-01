from django.core.exceptions import ValidationError


def file_size(file):
    limit = 2

    print(type(file))
    if file.size > limit * 1024 * 1024:
        raise ValidationError(f"File size must be lower than {limit}")
