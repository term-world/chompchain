import json
import random

users = [c for c in "abcdefghijklmnopqrstuvwxyz"]
cmds = ["pwd", "ls", "cd"]

for user in users:
    for cmd in cmds:
        if random.randint(0,1):
            content = {
                "user": user,
                "cmd": cmd
            }
            with open(f"{random.randint(1000,9999)}.json", "w") as fh:
                json.dump(content, fh)
