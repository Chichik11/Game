from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot
import datetime

TOKEN = '7354418372:AAE2Ucj7uxtDGXLk30hCf-2VDPt9TiFu5sY'

def get_profile_age(update, context):
    bot = Bot(TOKEN)
    user = bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
    joined_date = user.joined_date
    today = datetime.date.today()
    age = today - joined_date.date()
    return age.days

def give_coins(update, context):
    age = get_profile_age(update, context)
    if age < 30:
        coins = 10
    elif age < 60:
        coins = 20
    elif age < 90:
        coins = 30
    else:
        coins = 40
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'You have been awarded {coins} coins!')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('give_coins', give_coins))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
