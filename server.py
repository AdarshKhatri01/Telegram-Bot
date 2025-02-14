from flask import Flask
import threading
import bot
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=True, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()

    # Check karein ki bot pehle se run toh nahi ho raha
    if not os.path.exists("bot_running.lock"):
        open("bot_running.lock", "w").close()  # File create karein
        bot.main()