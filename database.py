import sqlite3
import time


DATABASE = "cellcity.db"



def connect():

    return sqlite3.connect(DATABASE)




def init_db():

    db = connect()

    cur = db.cursor()



    # Пользователи

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,

        nickname TEXT DEFAULT 'Игрок',

        role TEXT DEFAULT 'player',

        organization_id INTEGER DEFAULT 0,

        banned INTEGER DEFAULT 0

    )
    """)




    # Города

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(

        id INTEGER PRIMARY KEY,

        money INTEGER DEFAULT 1000,

        people INTEGER DEFAULT 0,

        happiness INTEGER DEFAULT 50,

        health INTEGER DEFAULT 100,

        safety INTEGER DEFAULT 50,

        reputation INTEGER DEFAULT 0,

        level INTEGER DEFAULT 1

    )
    """)




    # Организации

    cur.execute("""
    CREATE TABLE IF NOT EXISTS organizations(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        owner INTEGER,

        level INTEGER DEFAULT 1

    )
    """)




    # Участники организаций

    cur.execute("""
    CREATE TABLE IF NOT EXISTS organization_members(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        organization_id INTEGER,

        user_id INTEGER,

        rank TEXT DEFAULT 'worker'

    )
    """)




    # Здания

    cur.execute("""
    CREATE TABLE IF NOT EXISTS buildings(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        player_id INTEGER,

        x INTEGER,

        y INTEGER,

        type TEXT

    )
    """)




    # Чаты

    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        chat_type TEXT,

        organization_id INTEGER DEFAULT 0,

        message TEXT,

        created INTEGER

    )
    """)



    # Настройки админов

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings(

        key TEXT PRIMARY KEY,

        value TEXT

    )
    """)



    db.commit()

    db.close()






# ===================
# Пользователи
# ===================


def create_user(user_id):

    db = connect()

    cur = db.cursor()



    cur.execute("""

    INSERT OR IGNORE INTO users

    (
    id
    )

    VALUES(?)

    """,

    (
        user_id,
    ))


    db.commit()

    db.close()





def get_user(user_id):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    SELECT *

    FROM users

    WHERE id=?

    """,

    (
        user_id,
    ))


    result = cur.fetchone()


    db.close()


    return result






def set_role(

    user_id,

    role

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    UPDATE users

    SET role=?

    WHERE id=?

    """,

    (

    role,

    user_id

    ))


    db.commit()

    db.close()






def is_admin(user_id):

    user = get_user(user_id)


    if not user:

        return False


    return user[2] in [

        "admin",

        "owner",

        "moderator"

    ]






# ===================
# Чаты
# ===================


def add_message(

    user_id,

    chat_type,

    message,

    organization_id=0

):

    db = connect()

    cur = db.cursor()



    cur.execute("""

    INSERT INTO messages

    (

    user_id,

    chat_type,

    organization_id,

    message,

    created

    )

    VALUES(?,?,?,?,?)

    """,

    (

    user_id,

    chat_type,

    organization_id,

    message,

    int(time.time())

    ))



    db.commit()

    db.close()






def get_messages(

    chat_type,

    organization_id=0

):

    db = connect()

    cur = db.cursor()



    cur.execute("""

    SELECT

    user_id,

    message

    FROM messages

    WHERE

    chat_type=?

    AND organization_id=?

    ORDER BY id DESC

    LIMIT 20

    """,

    (

    chat_type,

    organization_id

    ))



    result = cur.fetchall()


    db.close()


    return result






# ===================
# Организации
# ===================


def create_organization(

    name,

    owner

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    INSERT INTO organizations

    (

    name,

    owner

    )

    VALUES(?,?)

    """,

    (

    name,

    owner

    ))



    org_id = cur.lastrowid



    cur.execute("""

    INSERT INTO organization_members

    (

    organization_id,

    user_id,

    rank

    )

    VALUES(?,?,?)

    """,

    (

    org_id,

    owner,

    "director"

    ))



    db.commit()

    db.close()



    return org_id
