import telegram
import schedule
import time
from datetime import datetime
from telegram import Bot

# Токен вашего бота и ID чата вашей девушки
TELEGRAM_TOKEN = '7285259289:AAElqGF4Q7t8EGx-ucBT6FvFZnoVwONdA9k'  # Замените на ваш токен бота
CHAT_ID = '-4206523570'  # Замените на ID чата вашей девушки

# Инициализация бота
bot = telegram.Bot(token=TELEGRAM_TOKEN)
def send_message():
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text='Привет, моя красотка! Это тестовое сообщение.')

    
if __name__ == '__main__':
    send_message()
    
# Функция для отправки сообщений
def send_message(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent message: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Планирование сообщений
def schedule_messages():
    # Утреннее сообщение
    schedule.every().day.at("08:00").do(send_message, message="Доброе утро, моя красотка")

    # Другие сообщения в течение дня
    schedule.every().day.at("12:00").do(send_message, message="Привет, как твой день?")
    schedule.every().day.at("15:00").do(send_message, message="Не забывай пить воду и кушать!")
    schedule.every().day.at("18:00").do(send_message, message="Как прошел твой день?")
    schedule.every().day.at("21:00").do(send_message, message="Спокойной ночи, милая!")
    schedule.every().day.at("13:30").do(send_message, message="Привет, как твой день?")

def main():
    # Настройка расписания сообщений
    schedule_messages()

    print("Starting scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
