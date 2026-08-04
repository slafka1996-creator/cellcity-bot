import sqlite3


def connect():
    return sqlite3.connect("cellcity.db")


def init_db():

    db = connect()
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(

        id INTEGER PRIMARY KEY,

        money INTEGER,

        people INTEGER,

        houses INTEGER

    )
    """)

    db.commit()
    db.close()



def create_player(user_id):

    db = connect()
    cur = db.cursor()


    cur.execute(
        """
        INSERT OR IGNORE INTO players
        VALUES(?,?,?,?)
        """,
        (
            user_id,
            1000,
            0,
            0
        )
    )


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
        (user_id,)
    )


    player = cur.fetchone()


    db.close()

    return player



def update_player(
    user_id,
    money,
    people,
    houses
):

    db = connect()
    cur = db.cursor()


    cur.execute(
        """
        UPDATE players

        SET money=?,
            people=?,
            houses=?

        WHERE id=?

        """,
        (
            money,
            people,
            houses,
            user_id
        )
    )


    db.commit()
    db.close()
