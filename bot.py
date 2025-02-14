import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext


load_dotenv()


# ✅ API KEYS
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 Hello! Mujhe ek prompt bhejo aur main AI image banaunga. 🎨")

async def generate_image(prompt):
    """ Hugging Face API se AI Image generate karega """
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        image_path = "output.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        return image_path
    return None

async def handle_message(update: Update, context: CallbackContext):
    prompt = update.message.text
    await update.message.reply_text("⏳ AI Image Generate Ho Raha Hai...")

    image_path = await generate_image(prompt)
    
    if image_path:
        await update.message.reply_photo(photo=open(image_path, "rb"))
    else:
        await update.message.reply_text("⚠ Image generate nahi ho payi! Dobara try karein.")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if _name_ == "_main_":
    main()