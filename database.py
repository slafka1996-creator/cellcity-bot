import sqlite3


def connect():

    return sqlite3.connect(
        "cellcity.db"
    )


def create_player(user_id):

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

    db=connect()

    cur=db.cursor()

    cur.execute(
        "SELECT * FROM players WHERE id=?",
        (user_id,)
    )

    result=cur.fetchone()

    db.close()

    return result
