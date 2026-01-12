import os, requests

TOKEN = os.environ["TG_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

text = "⏰ Erinnerung: Bitte vergiss nicht abzustimmen!"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": text
    },
    timeout=19
)
