from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = "abs_webhook_token_123"

@app.route("/")
def home():
    return "ABS WhatsApp Bot is Live (Railway)"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    print("INCOMING DATA 👇")
    print(request.json)
    return "ok", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
