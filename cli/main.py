import json
from audit.api import GitHubAPI
from audit.models import Follower
from audit.detectors import classify

def run(username, token=None):
    api = GitHubAPI(token)
    followers = api.get_followers(username)

    results = []
    dead_count = 0
    bot_count = 0

    # NEW: store usernames of flagged followers
    dead_list = []
    bot_list = []

    for f in followers:
        data = api.get_user(f["login"])
        follower = Follower(**data)
        result = classify(follower)
        results.append(result)

        if result["is_dead"]:
            dead_count += 1
            dead_list.append(follower.login)

        if result["is_bot"]:
            bot_count += 1
            bot_list.append(follower.login)

    total = len(followers)

    print(json.dumps({
        "username": username,
        "total_followers": total,
        "dead_followers_pct": round(dead_count / total * 100, 2),
        "bot_followers_pct": round(bot_count / total * 100, 2),

        # NEW: include flagged usernames
        "dead_followers": dead_list,
        "bot_followers": bot_list
    }, indent=2))
