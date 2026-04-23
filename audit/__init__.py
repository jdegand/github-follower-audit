from .api import GitHubAPI
from .models import Follower
from .scoring import score_dead, score_bot
from .detectors import classify

__all__ = [
    "GitHubAPI",
    "Follower",
    "score_dead",
    "score_bot",
    "classify",
]
