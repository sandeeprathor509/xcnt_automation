def fetching_query(*args):
    data = ""
    for arg in args:
        data += arg + " "
    query = "query{users{" + data + "}}"
    return query


def creation_query(**kwargs):
    creation = "mutation{createUser(input:" \
               "{email: " + '"' + kwargs.get("email") + '"'"" \
                                                        "firstName: " + '"' + kwargs.get("firstName") + '"'"" \
                                                                                                        "lastName: " + '"' + kwargs.get(
        "lastName") + '"' \
                      "newsletter: " + kwargs.get("newsletter") + "}){ok error}}"
    return creation


def delete_query(uuid):
    delete = "mutation{deleteUser(uuid:" + '"' + uuid + '"'"){ok}}"
    return delete


def update_query(**kwargs):
    api_update = "mutation{updateUser(input:" \
                 "{uuid: " + '"' + kwargs.get("uuid") + '"'" " \
                                                        "email: " + '"' + kwargs.get("email") + '"'" " \
                                                                                                "firstName: " + '"' + kwargs.get(
        "firstName") + '"'" " \
                       "lastName: " + '"' + kwargs.get("lastName") + '"'" " + \
                 "newsletter: " + kwargs.get("newsletter") + "}){ok}}".replace("\\", "")

    return api_update
