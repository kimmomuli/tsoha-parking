from flask import session
from app import app
from db import db
import user

def add_new(description, price, city, address):
    user_id = user.get_id()
    if user_id != 0:
        try:
            sql = "INSERT INTO parkinglot (owner_id, reserved, who_reserved_id, description , price, time, visible) \
                VALUES (:owner_id, 0, 0, :description, :price, NOW(), :visible)"
            db.session.execute(sql, {"owner_id":user_id, "description":description, "price":price, "visible":1})
            db.session.commit()
            sql = "SELECT id FROM parkinglot WHERE owner_id=:user_id AND description=:description AND price=:price AND visible=1"
            result = db.session.execute(sql, {"user_id":user_id, "description":description, "price":price})
            id = result.fetchone()[0]
            add_location(id, city, address)
            return True
        except:
            return False
    else:
        return False
        

def delete(id):
    try:
        sql = "UPDATE parkinglot SET visible=0 WHERE id=:park_id"
        db.session.execute(sql, {"park_id":id})
        db.session.commit()
        return True
    except:
        return False

def get_all():
    sql = "SELECT P.id, U.username, P.reserved, P.description, P.price, P.who_reserved_id, L.city, L.address \
        FROM location L, parkinglot P, users U \
        WHERE P.visible=1 AND owner_id = U.id AND P.id = L.parkinglot_id ORDER BY P.time"
    return db.session.execute(sql).fetchall()

def book(id):
    user_id = user.get_id()
    try:
        sql = "UPDATE parkinglot SET reserved=1, who_reserved_id=:user_id WHERE id=:park_id"
        db.session.execute(sql, {"user_id":user_id, "park_id":id})
        db.session.commit()
        return True
    except:
        return False

def stop_using(id):
    sql = "UPDATE parkinglot SET reserved=0, who_reserved_id=0 WHERE id=:park_id"
    db.session.execute(sql, {"park_id":id})
    db.session.commit()

def add_location(id, city, address):
    sql = "INSERT INTO location (parkinglot_id, city, address) VALUES (:parkinglot_id, :city, :address)"
    db.session.execute(sql, {"parkinglot_id":id, "city":city, "address":address})
    db.session.commit()

def city_results(city):
    sql = "SELECT L.city, L.address, P.id, U.username, P.reserved, P.description, P.price, P.who_reserved_id  \
        FROM location L, parkinglot P, users U \
        WHERE P.visible=1 AND owner_id = U.id AND P.id = L.parkinglot_id AND L.city=:city ORDER BY P.time"
    result = db.session.execute(sql, {"city":city})
    return result.fetchall()


def give_comment(parkking_lot_id, comment):
    try:
        user_id = user.get_id()
        sql = "INSERT INTO comments (parkinglot_id, user_id, comment) VALUES (:parkinglot_id, :user_id, :comment)"
        db.session.execute(sql, {"parkinglot_id":parkking_lot_id, "user_id":user_id, "comment":comment})
        db.session.commit()
        return True
    except:
        return False

def get_comment(id):
    sql = "SELECT U.username, C.comment FROM users U, comments C WHERE parkinglot_id=:id AND U.id = C.user_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_lot(id):
    sql = "SELECT U.username, P.reserved, P.description, P.price, L.city, L.address \
        FROM users U,parkinglot P, location L WHERE P.id=2 AND L.parkinglot_id = P.id AND U.id = P.owner_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def give_stars():
    pass