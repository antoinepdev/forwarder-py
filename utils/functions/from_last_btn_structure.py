def is_from_last_btn_structure(call, last_start_msg):
    try:
        last_btn_structure = last_start_msg + 1
        if call.message.id == last_btn_structure:
            return True
    except Exception as e:
        print(f"Error al comprobar si el btn event proviene del último btn structure: {e}")
    return False
