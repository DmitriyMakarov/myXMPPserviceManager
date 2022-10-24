from core.service import UserPasswordGenerator as up
from core.service import DataBase as db
from core.service import xmppApi as api

def newAccount():
    user = up.newUsername()
    password = up.newPassword()
    return user, password

def changePassword(user):
    password = up.newPassword()
    db.changePassword(user, password)
    api.changePassword(db.getXmppAccountInfo(user)[1], db.getXmppAccountInfo(user)[2])
    return password

def removeAccount(user):
    api.delAccount(db.getXmppAccountInfo(user)[1])
    db.hiddAccount(user)
