from bot_config import bot, admin_id
import os

@bot.message_handler(commands=["sendIDs"])
def send_ids(msg):
    if msg.chat.type != "private":
        return
    chat_id = msg.chat.id
    if chat_id != admin_id:
        return
    data_folder = os.path.join(os.path.dirname(__file__), "database", "data")
    movie_ids_path = os.path.join(data_folder, "movie_ids.json")
    user_ids_path = os.path.join(data_folder, "user_ids.json")
    try:
        with open(movie_ids_path, "rb") as movie_ids_json:
            bot.send_document(chat_id, movie_ids_json)
        with open(user_ids_path, "rb") as user_ids_json:
            bot.send_document(chat_id, user_ids_json)
    except Exception as e:
        print(f"Error al intentar enviar los archivos .json {e}")
