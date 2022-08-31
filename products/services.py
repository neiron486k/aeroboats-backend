def upload_media_path(instance, value: str):
    """Get upload path for media"""

    return "product/" + str(instance.pk) + "/" + value
