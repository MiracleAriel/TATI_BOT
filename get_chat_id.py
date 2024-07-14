from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

TELEGRAM_TOKEN = '7285259289:AAElqGF4Q7t8EGx-ucBT6FvFZnoVwONdA9k'  # Замените на ваш токен бота

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Ваш chat_id: {update.message.chat_id}')

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
