import datetime
import requests


class BaseWorker:

    def __init__(self, server_url: str):
        self.server_url = server_url
        self.end_points = {"check_login": self.server_url + "/users/check",
                           "users": self.server_url + "/users",
                           "posts": self.server_url + "/users/posts",
                      }

    def check_user_login(self, user: "User") -> "Login":
        resp = requests.get(url=self.end_points.get('check_login'), data=user.to_json())
        print(resp.text)
        return Login(user_id=resp.json()['id'], user_post=resp.json()['post_id'])

    def get_users_list(self):
        resp = requests.get(url=self.end_points.get('users'))
        return [User(user_id=user['id'], login=user['login'], reg_date=user['reg_date'], post=user['post'])
                for user in resp.json()]

    def get_posts_list(self):
        resp = requests.get(url=self.end_points.get('posts'))
        return [Post(post_id=post['id'], name=post['name']) for post in resp.json()]

    def add_new_user(self, user: "User"):
        resp = requests.post(url=self.end_points.get('users'), data=user.to_json())
        return resp.json()

    def delete_user(self, user_id: int):
        resp = requests.delete(url=self.end_points.get('users') + f'/{user_id}')
        return resp.json()

class Login:
    def __init__(self, user_id: int, user_post: int):
        self.user_id = user_id
        self.user_post = user_post


class User:
    def __init__(self, login: str, post: str = None, user_id: int = None, reg_date: str = None, post_id: int = 0,
                 password: str = None):
        self.user_id = user_id
        self.login = login
        if reg_date:
            self.reg_date = datetime.datetime.strptime(reg_date, '%Y-%m-%dT%H:%M:%S')
        self.post = post
        self.post_id = post_id
        self.password = password

    def to_json(self):
        return f'{{"login": "{self.login}", "password": "{self.password}", "post_id": {self.post_id}}}'


class Post:
    def __init__(self, post_id: int, name: str):
        self.post_id = post_id
        self.name = name
