import pytest
from datetime import datetime, timedelta, timezone

from audit.detectors import classify
from audit.models import Follower

def make_user(**kwargs):
    defaults = {
        "login": "bot123xyz",
        "created_at": (datetime.now(timezone.utc) - timedelta(days=5)).isoformat(),
        "updated_at": (datetime.now(timezone.utc) - timedelta(days=500)).isoformat(),
        "public_repos": 0,
        "public_gists": 0,
        "followers": 1,
        "following": 500,
        "avatar_url": "https://github.com/images/error/avatar.png",
        "bio": "",
    }
    defaults.update(kwargs)
    return Follower(**defaults)

# ------------------------------------------------------------
# 1. Structure test — ensures API stability
# ------------------------------------------------------------
def test_classify_structure():
    user = make_user()
    result = classify(user)

    assert set(result.keys()) == {
        "dead_score",
        "bot_score",
        "is_dead",
        "is_bot",
    }


# ------------------------------------------------------------
# 2. Threshold consistency — ensures boolean logic matches scores
# ------------------------------------------------------------
def test_classify_threshold_consistency():
    user = make_user()
    result = classify(user)

    assert result["is_dead"] == (result["dead_score"] >= 70)
    assert result["is_bot"] == (result["bot_score"] >= 60)


# ------------------------------------------------------------
# 3. Monotonicity tests — stable even when scoring changes
# ------------------------------------------------------------
def test_bot_score_increases_with_bot_signals():
    base = make_user(followers=10, following=10)
    more_bot = make_user(followers=0, following=2000)

    base_score = classify(base)["bot_score"]
    bot_score = classify(more_bot)["bot_score"]

    assert bot_score > base_score


def test_dead_score_increases_with_stale_update():
    fresh = make_user(updated_at=datetime.now(timezone.utc).isoformat())
    stale = make_user(updated_at="2000-01-01T00:00:00Z")

    fresh_score = classify(fresh)["dead_score"]
    stale_score = classify(stale)["dead_score"]

    assert stale_score > fresh_score
