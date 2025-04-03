from bot_config import bot, admin_id
import os


@bot.message_handler(commands=["deleteMe"])
def delete_me(msg):
    if msg.chat.type != "private":
        return
    chat_id = msg.chat.id
    if chat_id != admin_id:
        return
    data_folder = os.path.join(os.path.dirname(__file__), "database", "data")
    user_ids_path = os.path.join(data_folder, "user_ids.json")
    try:
        with open(user_ids_path, "rb") as id_list:
            bot.send_document(chat_id, user_ids_json)
    except Exception as e:

