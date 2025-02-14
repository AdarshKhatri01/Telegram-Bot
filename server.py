from flask import Flask
import threading
import bot  # bot.py ko import kar rahe hain

app = Flask(_name_)

@app.route('/')
def home():
    return "Bot is running!"

# Flask ko alag thread pe run karein
def run_flask():
    app.run(host="0.0.0.0", port=8080)

if _name_ == "_main_":
    threading.Thread(target=run_flask).start()
    bot.main()  # bot.py ka main() function call karein