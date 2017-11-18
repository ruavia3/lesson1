from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format="%(name)s -%(levelname)s-%(message)s",
    level=logging.INFO,
    filename="bot.log"
    )

def greet_user(bot, update):
    text = "Вызван /start"
    print(text)
  #  print (1/0)

    update.message.reply_text(text)
    #print("Вызван /start")
    #print(update)

def talk_to_me(bot, update):
    user_text=update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text + "?")

def main():
    updater = Updater("460984466:AAE8eUWEA-hLEO3rkQ03xpJRm0StI8Wk_VA")
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()

main()