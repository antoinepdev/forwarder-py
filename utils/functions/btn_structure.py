from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


def inline_keyboard(bot, chat_id, referral_link, msg_instructor):
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(
        "Activar acceso",
        url=referral_link
    )
    btn2 = InlineKeyboardButton(
        "Obtener Película",
        callback_data= "register"
    )
    markup.add(btn1, btn2)
    bot.send_message(chat_id, msg_instructor, reply_markup=markup)
