from src.server.database import base_manager

def get_groups():
    res = base_manager.execute("SELECT id, name FROM groups")
    print(res)
    return res

def add_group(name: str):
    res = base_manager.execute("INSERT INTO groups(name) "
                               "VALUES (?) "
                               "RETURNING id", args=(name, ))
    return res