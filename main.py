from telebot import TeleBot
import settings, telegram_bot


bot = TeleBot(settings.TOKKEN_BOT)

joke_bot = telegram_bot.TelegramBot(bot)


@bot.message_handler(commands=['start'])
def start(message):
    joke_bot.start(message)




@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke_bot.send_joke(message)


@bot.message_handler(content_types=['text'])
def send_text_relpy(message):
    joke_bot.send_joke(message)


@bot.message_handler(content_types=['photo', 'sticker', 'audio', 'pinned_message', 'document'])
def send_not_text_reply(message):
    joke_bot.send_not_text_reply(message)



bot.polling(none_stop=True)