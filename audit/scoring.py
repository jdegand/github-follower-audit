from .utils import days_since, username_entropy

def score_dead(user):
    score = 0
    if days_since(user.updated_at) > 365:
        score += 40
    if user.public_repos == 0:
        score += 20
    if user.public_gists == 0:
        score += 10
    if user.avatar_url.endswith("avatar.png"):
        score += 10
    if not user.bio:
        score += 10
    if user.followers == 0:
        score += 10
    return score

def score_bot(user):
    score = 0
    if username_entropy(user.login) > 3.5:
        score += 30
    if user.following > 200:
        score += 20
    if user.followers > 0 and (user.followers / max(1, user.following)) < 0.05:
        score += 20
    if days_since(user.created_at) < 30:
        score += 20
    if user.public_repos == 0:
        score += 10
    return score
