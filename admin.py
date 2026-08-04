from database import *
from database import connect



# =====================
# Проверка доступа
# =====================


def admin_access(user_id):

    if is_admin(user_id):

        return True

    return False





# =====================
# Главное меню админа
# =====================


def admin_menu(user_id):


    if not admin_access(user_id):

        return """

⛔ Доступ запрещён.

"""



    return """

🔐 Панель администратора


Команды:


👥 игроки

💰 выдать ID сумма

👑 роль ID admin

🚫 бан ID

✅ разбан ID

📢 рассылка текст


"""







# =====================
# Список игроков
# =====================


def show_players(user_id):


    if not admin_access(user_id):

        return "⛔ Нет доступа"



    db = connect()

    cur = db.cursor()



    cur.execute("""

    SELECT id, nickname, role

    FROM users

    LIMIT 30

    """)



    players = cur.fetchall()


    db.close()



    text = """

👥 Игроки:

"""


    for p in players:


        text += f"""

ID:
{p[0]}

👤 {p[1]}

Роль:
{p[2]}

----------------

"""



    return text






# =====================
# Выдать деньги
# =====================


def give_money(

        admin_id,

        player_id,

        amount

):


    if not admin_access(admin_id):

        return "⛔ Нет доступа"



    db = connect()

    cur = db.cursor()



    cur.execute("""

    UPDATE players

    SET money = money + ?

    WHERE id=?

    """,

    (

    amount,

    player_id

    ))



    db.commit()

    db.close()



    return f"""

✅ Деньги выданы.


Игрок:
{player_id}


Сумма:
💰 {amount}

"""







# =====================
# Выдать роль
# =====================


def change_role(

        admin_id,

        player_id,

        role

):


    if not admin_access(admin_id):

        return "⛔ Нет доступа"



    set_role(

        player_id,

        role

    )


    return f"""

✅ Роль изменена.


Игрок:
{player_id}


Новая роль:
{role}

"""







# =====================
# Бан
# =====================


def ban_player(

        admin_id,

        player_id

):


    if not admin_access(admin_id):

        return "⛔ Нет доступа"



    db = connect()

    cur = db.cursor()



    cur.execute("""

    UPDATE users

    SET banned=1

    WHERE id=?

    """,

    (

    player_id,

    ))



    db.commit()

    db.close()



    return """

🚫 Игрок заблокирован.

"""







# =====================
# Разбан
# =====================


def unban_player(

        admin_id,

        player_id

):


    if not admin_access(admin_id):

        return "⛔ Нет доступа"



    db = connect()

    cur = db.cursor()



    cur.execute("""

    UPDATE users

    SET banned=0

    WHERE id=?

    """,

    (

    player_id,

    ))



    db.commit()

    db.close()



    return """

✅ Игрок разблокирован.

"""
