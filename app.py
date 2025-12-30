from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "abs_webhook_token_123"

@app.route("/", methods=["GET"])
def home():
    return "ABS WhatsApp Bot is Live (Railway)"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    print("INCOMING DATA 👇")
    print(request.json)
    return "ok", 200
