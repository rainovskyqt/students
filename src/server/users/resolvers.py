from datetime import datetime
from typing import List

from .models import User, InputUser, NewId, Post
from database.db_manager import base_manager

def check_user(login: InputUser) -> User:
    res = base_manager.execute("SELECT id, post_id "
                               "FROM users "
                               "WHERE login= ? AND password = ?", args=(login.login.lower(), login.password), many=False)
    print(res)
    if res['data']:
        return User(id=res['data'][0], post_id=res['data'][1])
    else:
        return User(id=0, post_id=0)


def get_users():
    res = base_manager.execute("SELECT U.id, U.login, datetime(U.reg_date, 'unixepoch', 'localtime'), P.id, P.name "
                               "FROM users U "
                               "INNER JOIN posts P ON U.post_id = P.id", many=True)
    users = []                      #Сделано более медленным способом и в лоб
    for user in res['data']:
        print()
        users.append(User(id=user[0], login=user[1], reg_date=datetime.strptime(user[2],'%Y-%m-%d %H:%M:%S'),
                     post_id=user[3], post=user[4]))
    return users


def add_new_user(new_user: InputUser):
    res = base_manager.execute("INSERT INTO users(login, password, post_id) "
                               "VALUES (?, ?, ?) "
                               "RETURNING id", args=(new_user.login.lower(), new_user.password, new_user.post_id))
    return NewId(code=res['code'], id=res['data'][0][0])


def delete_current_user(user_id: int):
    res = base_manager.execute("DELETE FROM users WHERE id = ?",
                               args=(user_id,))
    return NewId(code=res['code'], id=user_id)


def get_posts() -> List[{Post}]:
    res = base_manager.execute("SELECT id, name "
                               "FROM posts")
    # Сделано с использованием генератора списка
    return [Post(id=post[0], name=post[1]) for post in res['data']]
