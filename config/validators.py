from django.core.exceptions import ValidationError


def file_size(file):
    limit = 2

    if file.size > limit * 1024 * 1024:
        raise ValidationError(f"File size must be lower than {limit}")


def allowed_file_extension() -> list[str]:
    return ["png", "webp", "jpg", "jpeg", "mp4", "mpv"]
