from pathlib import Path


def upload_slide_path(_, filename: str) -> str:
    """Get upload path for slide model"""

    return Path.joinpath("slide", filename)
