def upload_slide_path(_, filename: str) -> str:
    """Get upload path for slide model"""

    return "slides/" + filename
