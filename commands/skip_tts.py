BOT_USERNAMES = ["pochamabot", "sery_bot"]

def run():
    return "$username" not in BOT_USERNAMES and "$message"[0] == "!" or "$message"[0] == "@"

print(run())