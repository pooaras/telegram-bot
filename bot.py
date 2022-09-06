from asyncore import dispatcher
from telegram import *
from telegram.ext import *
import telegram.ext

token="5337670068:AAHZfBXkcziWkf0jOpa8qqJS7YgzfE0SAFg"
updater=telegram.ext.Updater(token,use_context=True)
dispatcher=updater.dispatcher


def start(update,context):
    update.message.reply_text("hi I lov")




dispatcher.add_handler(telegram.ext.CommandHandler("start",start))


updater.start_polling()
updater.idle()