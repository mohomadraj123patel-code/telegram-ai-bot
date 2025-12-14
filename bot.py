import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# ====== KEYS (yaha apni key dalna) ======
TELEGRAM_BOT_TOKEN = "8227971586:AAEGtWdW0Zqjf2SOgdEk8Os0YVWya1PqoC0"
OPENAI_API_KEY = "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"

# ====== OpenAI function ======
def ask_openai(question):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# ====== Start command ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 AI Bot Live hai! Message bhejo.")

# ====== Message reply ======
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    answer = ask_openai(user_text)
    await update.message.reply_text(answer)

# ====== Main ======
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == "__main__":
    main()

