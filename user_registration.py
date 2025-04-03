from bot_config import bot, referral_link, storage_id
from utils.functions.btn_structure import inline_keyboard
from utils.functions.from_last_btn_structure import is_from_last_btn_structure
from utils.messages import msg_instructor, msg_soon_access
from database.find_id import find_id
from database.save_id import save_id

def registration_process(msg, movie_id):
    chat_id = msg.chat.id
    inline_keyboard(bot, chat_id, referral_link, msg_instructor)


    @bot.callback_query_handler(func= lambda x: True)
    def answer_btn(call):
        if call.data == "register":
            last_start_msg = msg.message_id
            if is_from_last_btn_structure(call, last_start_msg):
                user_on_database = find_id(chat_id, "user")
                if user_on_database:
                    try:
                        bot.delete_message(chat_id, last_start_msg+2)
                        bot.delete_message(chat_id, last_start_msg+1)
                    except Exception as e:
                        print(f"Error al intentar eliminar el mensaje: {e}")
                    try:
                        bot.copy_message(chat_id, storage_id, movie_id)
                        bot.answer_callback_query(call.id, "Archivo Enviado")
                        return
                    except Exception as e:
                        print(f"Error al intentar reenviarle el archivo al usuario {e}")
                else:
                    try:
                        bot.send_message(chat_id, msg_soon_access)
                        save_id(chat_id, "user")
                    except Exception as e:
                        print(f"Error al intentar enviarle un mensaje al usuario: {e}")
                    bot.answer_callback_query(call.id, "Necesitas completar el paso previo.")

