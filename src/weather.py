from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pytz
from datetime import datetime
import os


# Replace 'YOUR_BOT_TOKEN' with your actual token
TOKEN="TOKEN:TOKEN:Ls"
TOKEN = os.getenv('BOT_TOKEN')
# Define a list of some common city timezones
city_timezones = {
    'new_york': 'America/New_York',
    'london': 'Europe/London',
    'tokyo': 'Asia/Tokyo',
    'sydney': 'Australia/Sydney',
    'paris': 'Europe/Paris',
    'moscow': 'Europe/Moscow',
    'beijing': 'Asia/Shanghai'
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello! I can provide the current date in different cities around the world.\n"
        "Use the /date command followed by the city name.\n\n"
        "Example:\n"
        "/date tokyo\n"
        "Available cities: " + ', '.join(city_timezones.keys())
    )

def get_date(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text("Please provide a city name. Example: /date london")
        return

    city = context.args[0].lower()
    if city in city_timezones:
        tz = pytz.timezone(city_timezones[city])
        city_time = datetime.now(tz)
        date_str = city_time.strftime('%Y-%m-%d')
        update.message.reply_text(f"The current date in {city.capitalize()} is: {date_str}")
    else:
        update.message.reply_text("City not found. Available cities: " + ', '.join(city_timezones.keys()))

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("date", get_date))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

