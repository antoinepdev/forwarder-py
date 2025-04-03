import json
movie_ids_path = "database/data/movie_ids.json"
user_ids_path = "database/data/user_ids.json"


def find_id(recived_id, id_type):
    try:
        path = movie_ids_path if id_type == "movie" else user_ids_path
        with open(path, "r") as data:
            ids_list = json.load(data)
        if recived_id in ids_list:
            return True
    except Exception as e:
        print(f"Error al intentar buscar el id({recived_id} en la BD: {e})")
    return False
