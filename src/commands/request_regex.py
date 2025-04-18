import re

def run():
    can_you_play = re.compile(r"(?:can\s(?:yo)?u)?\s(?:play|do).*")
    do_this_pls = re.compile(r"do.*pl(?:s|ease)")

    return re.search(can_you_play, "$message") is not None or re.search(do_this_pls, "$message") is not None


print(run())