import math
from datetime import datetime, timezone

def days_since(dt):
    if isinstance(dt, str):
        # Convert GitHub ISO8601 string to aware datetime
        dt = datetime.fromisoformat(dt.replace("Z", "+00:00"))

    # Use timezone-aware "now"
    now = datetime.now(timezone.utc)

    return (now - dt).days

def username_entropy(username):
    # Shannon entropy
    freq = {c: username.count(c) for c in set(username)}
    total = len(username)
    return -sum((count/total) * math.log2(count/total) for count in freq.values())
