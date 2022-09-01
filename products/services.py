def upload_media_path(_, filename: str) -> str:
    """Get upload path for media model"""

    return "products/" + filename
