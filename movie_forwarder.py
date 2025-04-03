from bot_config import bot, storage_id
from utils.functions.get_id import get_id
from database.find_id import find_id
from user_registration import registration_process


@bot.message_handler(commands=["start"])
def start(msg):
    chat_id = msg.chat.id
    if msg.chat.type != "private":
        return
    movie_id = get_id(msg.text)
    if movie_id is None:
        bot.send_message(chat_id, "Enlace incorrecto")
        return
    id_on_database = find_id(movie_id, "movie")
    if not id_on_database:
        bot.send_message(
            chat_id, "Peli eliminada por copyright, informa al admin del grupo para que la resuba")
        return
    user_on_database = find_id(chat_id, "user")
    if user_on_database:
        try:
            bot.copy_message(chat_id, storage_id, movie_id)
        except Exception as e:
            print(f"Error al intentar reenviarle el archivo al usuario {e}")
        return
    registration_process(msg, movie_id)
