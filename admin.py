from flask import session
from db import db

def get_users():
    sql = "SELECT id, username, admin FROM users WHERE visible=1"
    return db.session.execute(sql).fetchall()

def delete_user(id):
    try:
        sql = "UPDATE users SET visible = 0 WHERE id=:user_id"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
        return True
    except:
        return False