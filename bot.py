import telebot
from flask import Flask, request

# Your bot token from BotFather
TOKEN = "7978434778:AAFUtsQeDvdqZfNAfXD92MIHEQurRDT98C8"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Reply system
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Drone & DJ Lover Bot 🤖\nAsk me anything!")

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    text = message.text.lower()
    
    if "drone" in text:
        bot.reply_to(message, "Our drones are equipped with HD + Thermal cameras 🚁🔥")
    elif "dj" in text:
        bot.reply_to(message, "DJ mixing tutorials coming soon 🎶🔥")
    elif "hi" in text or "hello" in text:
        bot.reply_to(message, "Hi! How can I help you today?")
    else:
        bot.reply_to(message, "Sorry, I didn’t understand that. Please try again!")

# Webhook for Render
@app.route(f"/{TOKEN}", methods=["POST"])
def getMessage():
    json_str = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://your-render-app.onrender.com/{TOKEN}")
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
