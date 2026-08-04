import sqlite3
import time


DATABASE = "cellcity.db"



def connect():

    return sqlite3.connect(
        DATABASE
    )



def init_db():

    db = connect()

    cur = db.cursor()


    # Игроки и города

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



    # Профессии жителей

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs(

        player_id INTEGER PRIMARY KEY,

        guides INTEGER DEFAULT 0,

        guards INTEGER DEFAULT 0,

        medics INTEGER DEFAULT 0,

        doctors INTEGER DEFAULT 0,

        radio INTEGER DEFAULT 0

    )
    """)



    # Общий чат

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        message TEXT,

        created INTEGER

    )
    """)



    db.commit()

    db.close()





# -----------------------
# Игрок
# -----------------------


def create_player(user_id):

    db = connect()

    cur = db.cursor()



    cur.execute(
    """
    INSERT OR IGNORE INTO players

    (
    id,
    money,
    people,
    happiness,
    health,
    safety,
    reputation,
    level
    )

    VALUES(?,?,?,?,?,?,?,?)

    """,

    (
        user_id,
        1000,
        0,
        50,
        100,
        50,
        0,
        1
    ))



    cur.execute(
    """
    INSERT OR IGNORE INTO jobs

    (
    player_id
    )

    VALUES(?)

    """,

    (
        user_id,
    ))



    db.commit()

    db.close()





def get_player(user_id):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """
    SELECT *

    FROM players

    WHERE id=?

    """,

    (
        user_id,
    ))


    result = cur.fetchone()


    db.close()


    return result






def update_player(

    user_id,

    money,

    people,

    happiness,

    health,

    safety,

    reputation,

    level

):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    UPDATE players

    SET

    money=?,

    people=?,

    happiness=?,

    health=?,

    safety=?,

    reputation=?,

    level=?

    WHERE id=?

    """,

    (

    money,

    people,

    happiness,

    health,

    safety,

    reputation,

    level,

    user_id

    ))



    db.commit()

    db.close()





# -----------------------
# Профессии
# -----------------------


def get_jobs(user_id):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    SELECT *

    FROM jobs

    WHERE player_id=?

    """,

    (
        user_id,
    ))


    result = cur.fetchone()


    db.close()


    return result





def update_jobs(

    user_id,

    guides,

    guards,

    medics,

    doctors,

    radio

):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    UPDATE jobs

    SET

    guides=?,

    guards=?,

    medics=?,

    doctors=?,

    radio=?

    WHERE player_id=?

    """,

    (

    guides,

    guards,

    medics,

    doctors,

    radio,

    user_id

    ))



    db.commit()

    db.close()






# -----------------------
# Здания
# -----------------------


def add_building(

    user_id,

    x,

    y,

    building_type

):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    INSERT INTO buildings

    (
    player_id,
    x,
    y,
    type
    )

    VALUES(?,?,?,?)

    """,

    (

    user_id,

    x,

    y,

    building_type

    ))


    db.commit()

    db.close()





def get_buildings(user_id):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    SELECT x,y,type

    FROM buildings

    WHERE player_id=?

    """,

    (
        user_id,
    ))


    result = cur.fetchall()


    db.close()


    return result





# -----------------------
# Общий чат
# -----------------------


def add_chat_message(

    user_id,

    message

):

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    INSERT INTO chat

    (
    user_id,
    message,
    created
    )

    VALUES(?,?,?)

    """,

    (

    user_id,

    message,

    int(time.time())

    ))


    db.commit()

    db.close()






def get_chat():

    db = connect()

    cur = db.cursor()


    cur.execute(
    """

    SELECT user_id,message

    FROM chat

    ORDER BY id DESC

    LIMIT 10

    """
    )


    result = cur.fetchall()


    db.close()


    return result
