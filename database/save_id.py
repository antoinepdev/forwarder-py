import json
movie_ids_path = "database/data/movie_ids.json"
user_ids_path = "database/data/user_ids.json"


def save_id(recived_id, id_type):
    path = movie_ids_path if id_type == "movie" else user_ids_path

    try:
        with open(path, "r") as file:
            ids_list = json.load(file)
        ids_list.append(recived_id)

        with open(path, "w") as file:
            json.dump(ids_list, file)
    except Exception as e:
        print(f"Ocurrió un error al intentar guardar el id: {
              recived_id} en la base de datos: {e}")
        return False
    return True
