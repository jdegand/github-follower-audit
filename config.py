# Thresholds for classification
DEAD_THRESHOLD = 70
BOT_THRESHOLD = 60

# Dead follower scoring weights
DEAD_WEIGHTS = {
    "inactive_days": 40,
    "no_repos": 20,
    "no_gists": 10,
    "default_avatar": 10,
    "empty_bio": 10,
    "no_followers": 10,
}

# Bot-like scoring weights
BOT_WEIGHTS = {
    "high_entropy": 30,
    "mass_following": 20,
    "ratio_anomaly": 20,
    "new_account": 20,
    "no_repos": 10,
}

# Heuristic thresholds
INACTIVE_DAYS = 365
USERNAME_ENTROPY_THRESHOLD = 3.5
MASS_FOLLOWING_THRESHOLD = 200
NEW_ACCOUNT_DAYS = 30
FOLLOW_RATIO_MIN = 0.05
