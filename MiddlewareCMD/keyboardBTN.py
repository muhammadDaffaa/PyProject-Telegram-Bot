from telegram import ReplyKeyboardMarkup, KeyboardButton


class MiddlewareBTN:

    def __init__(self):
        self.buttons = [
            [KeyboardButton('Guess Number 🎲')],
            # [KeyboardButton('Button 2'), KeyboardButton('Button 3')],
        ]
        self.reply_markup = ''

    def get_keyboard_buttons(self):
        return self.buttons

    def get_keyboard_mark_up(self):
        self.reply_markup = ReplyKeyboardMarkup(self.buttons, resize_keyboard=True, one_time_keyboard=True)
        return self.reply_markup
