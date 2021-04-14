from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username AND visible = 1"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else: 
        if check_password_hash(user[0], password):
            session["username"] = username
            session["user_id"] = user[1]
            return True
        else:
            return False
            
def logout():
    del session["username"]
    del session["user_id"]

def create(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, admin, visible) VALUES (:username,:password,:admin,:visible)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":0, "visible":1})
        db.session.commit()
    except:
        return False
    return login(username, password)

def is_admin():
    sql = "SELECT admin FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":get_id()})
    if result.fetchall()[0][0] == 1:
        return True
    else:
        return False

def get_id():
    return session.get("user_id",0)

def get_own_parking_lots():
    id = get_id()
    sql = "SELECT id, reserved, description , price FROM parkinglot WHERE owner_id=:user_id AND visible=1"
    result =  db.session.execute(sql, {"user_id": id})
    return result.fetchall()