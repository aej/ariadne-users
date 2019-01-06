from pydantic import ValidationError

from db import users_db
from .types import User


def get_user_resolver(_, info, id):
    user = [u for u in users_db if u.id == id]
    if len(user) == 1:
        return user[0]
    return None


def create_user_resolver(_, info, email, firstName, lastName):
    new_user = {"email": email, "firstName": firstName, "lastName": lastName}

    try:
        User(**new_user)
    except ValidationError as e:
        error_list = []
        for err in e.errors():
            new_err = {"path": err["loc"][0], "message": err["msg"]}
            error_list.append(new_err)
        return {"errors": error_list}

    if len(users_db) == 0:
        user_exists = False
    else:
        user_exists = len([u for u in users_db if u.email == email]) > 0

    if user_exists:
        error_list = [
            {"path": "email", "message": "User with this email address already exists"}
        ]
        return {"errors": error_list}

    if len(users_db) == 0:
        next_id = 1
    else:
        next_id = max([u.id for u in users_db]) + 1

    new_user["id"] = next_id
    user = User(id=next_id, email=email, firstName=firstName, lastName=lastName)
    users_db.append(user)

    return {"user": dict(user)}


def list_users_resolver(_, info):
    return users_db


user_resolvers = {
    "Query": {"getUser": get_user_resolver, "listUsers": list_users_resolver},
    "Mutation": {"createUser": create_user_resolver},
}
