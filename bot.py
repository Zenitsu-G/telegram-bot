from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

8726897978:AAGXPv3nezhg7lpkzKw8GDOErHK6RELgMLw = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
