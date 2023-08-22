import requests, time, random
from telebot import types
import settings, translate_text


class TelegramBot:

    def __init__(self, bot) -> None:

        self.bot = bot
        self.is_send_message = False



    def start(self, message):

        if self.is_send_message:
            self.send_wait_message(message)
            return

        self.toggle_is_send_message()

        chat_id = self.get_chat_id(message)
        user_name = self.get_user_name(message)
        user_language = self.get_user_language(message)

        markup = types.InlineKeyboardMarkup()
        markup.add( types.InlineKeyboardButton(translate_text.translate_text('github', user_language), url='https://habr.com/ru/all/'))

        self.bot.send_message(chat_id, translate_text.translate_text(f'Hi {user_name} good to see you, I`m a joker bot I can tell a joke \n just ask me to tell a joke and I will tell \n \n all source code is published on github (do not forget to put an asterisk, I will be very grateful 🥰)', user_language), reply_markup=markup)

        self.toggle_is_send_message()



    def send_joke(self, message):

        if self.is_send_message:
            self.send_wait_message(message)
            return

        self.toggle_is_send_message()


        chat_id = self.get_chat_id(message)
        user_language = self.get_user_language(message)

        joke = self.get_joke()
        list_emojys = ['🤣', '🤡', '😂', '🤓', '😜']


        self.bot.send_message(chat_id,  translate_text.translate_text(joke['setup'], user_language))
        time.sleep(5)

        self.bot.send_message(chat_id,  translate_text.translate_text(joke['punchline'], user_language))
        time.sleep(1)

        self.bot.send_message(chat_id, list_emojys[random.randint(0, len(list_emojys) - 1)])

        self.toggle_is_send_message()



    def send_wait_message(self, message):

        chat_id = self.get_chat_id(message)
        user_language = self.get_user_language(message)

        self.bot.send_message(chat_id, translate_text.translate_text('Wait until i tell the joke to the end 😡', user_language))



    def send_not_text_reply(self, message):

        chat_id = self.get_chat_id(message)
        user_language = self.get_user_language(message)

        self.bot.send_message(chat_id, translate_text.translate_text('What you sent is great, but you know what`s better than this? Joker bot jokes! 🤡', user_language))



    def toggle_is_send_message(self):

        self.is_send_message = not(self.is_send_message)



    def get_joke(self):

        joke = requests.get(settings.JOKES_DATA_PATH).json()

        return {'setup': joke['setup'], 'punchline': joke['punchline']}
    


    def get_user_name(self, message):

        return message.from_user.first_name
    


    def get_chat_id(self, message):

        return message.chat.id
    


    def get_user_language(self, message):

        return message.from_user.language_code

    
    