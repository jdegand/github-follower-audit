from .scoring import score_dead, score_bot

def classify(user):
    dead_score = score_dead(user)
    bot_score = score_bot(user)

    return {
        "dead_score": dead_score,
        "bot_score": bot_score,
        "is_dead": dead_score >= 70,
        "is_bot": bot_score >= 60,
    }
