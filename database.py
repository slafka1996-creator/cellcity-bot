import sqlite3


DATABASE = "cellcity.db"



def connect():

    return sqlite3.connect(
        DATABASE
    )



def init_db():

    db = connect()

    cur = db.cursor()


    # Игроки

    cur.execute("""

    CREATE TABLE IF NOT EXISTS players(

        id INTEGER PRIMARY KEY,

        money INTEGER DEFAULT 1000,

        people INTEGER DEFAULT 0,

        happiness INTEGER DEFAULT 50,

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



    db.commit()

    db.close()




def create_player(
        user_id
):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    INSERT OR IGNORE INTO players

    (
        id,
        money,
        people,
        happiness,
        level
    )

    VALUES(?,?,?,?,?)

    """,

    (
        user_id,
        1000,
        0,
        50,
        1
    ))


    db.commit()

    db.close()




def get_player(
        user_id
):

    db = connect()

    cur = db.cursor()


    cur.execute("""

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

        level

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    UPDATE players

    SET

    money=?,

    people=?,

    happiness=?,

    level=?

    WHERE id=?

    """,

    (

        money,

        people,

        happiness,

        level,

        user_id

    ))


    db.commit()

    db.close()





def add_building(

        user_id,

        x,

        y,

        building_type

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

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





def get_buildings(

        user_id

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    SELECT

    x,

    y,

    type

    FROM buildings

    WHERE player_id=?

    """,

    (

        user_id,

    ))


    result = cur.fetchall()


    db.close()


    return result





def building_exists(

        user_id,

        x,

        y

):

    db = connect()

    cur = db.cursor()


    cur.execute("""

    SELECT id

    FROM buildings

    WHERE

    player_id=?

    AND x=?

    AND y=?

    """,

    (

        user_id,

        x,

        y

    ))


    result = cur.fetchone()


    db.close()


    return result is not None
