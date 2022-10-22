from core.service import UserPasswordGenerator as up
from core.service import DataBase as db
from core.service import xmppApi as api

def newAccount(user_id):
    user = up.newUsername()
    password = up.newPassword()
    db.newAccount(user_id, user, password)
    return user, password