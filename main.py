import os

PICKUP = "I've been saving your favourite chocolate behind this glass all day. Press B4 and I'll drop it like it's hot — exact change only, my heart runs on coins."

def drop_line():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as chute:
        chute.write(PICKUP)

drop_line()
