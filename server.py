from flask import Flask
import subprocess
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Flask Server ko Run Karein
def run_flask():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    # Bot sirf ek hi baar chale, iske liye process check karein
    while True:
        # Check karein ki bot chal raha hai ya nahi
        bot_running = os.popen("pgrep -f bot.py").read().strip()
        
        if not bot_running:
            print("🚀 Starting bot...")
            subprocess.Popen(["python", "bot.py"])  # Bot start karein

        time.sleep(10)  # 10 second me ek baar check karein