from database import *
from database import connect




# =========================
# Создание организации
# =========================


def create_org(

        user_id,

        name

):


    create_user(
        user_id
    )


    user = get_user(
        user_id
    )


    if user[3] != 0:


        return """

❌ Вы уже состоите в организации.

"""



    org_id = create_organization(

        name,

        user_id

    )



    db = connect()

    cur = db.cursor()



    cur.execute("""

    UPDATE users

    SET organization_id=?

    WHERE id=?

    """,

    (

    org_id,

    user_id

    ))



    db.commit()

    db.close()



    return f"""

🏢 Организация создана!


Название:

{name}


Вы директор.

"""







# =========================
# Вступить
# =========================


def join_org(

        user_id,

        org_id

):


    create_user(
        user_id
    )


    db = connect()

    cur = db.cursor()



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

    user_id,

    "worker"

    ))



    cur.execute("""

    UPDATE users

    SET organization_id=?

    WHERE id=?

    """,

    (

    org_id,

    user_id

    ))



    db.commit()

    db.close()



    return """

✅ Вы вступили в организацию.

"""







# =========================
# Информация
# =========================


def organization_info(

        user_id

):


    user = get_user(
        user_id
    )


    if not user or user[3]==0:


        return """

❌ Вы не состоите в организации.

"""



    org_id = user[3]



    db = connect()

    cur = db.cursor()



    cur.execute("""

    SELECT

    name,

    owner,

    level

    FROM organizations

    WHERE id=?

    """,

    (

    org_id,

    ))



    org = cur.fetchone()



    cur.execute("""

    SELECT COUNT(*)

    FROM organization_members

    WHERE organization_id=?

    """,

    (

    org_id,

    ))



    members = cur.fetchone()[0]



    db.close()



    return f"""

🏢 Организация


Название:

{org[0]}


👑 Директор:

{org[1]}


⭐ Уровень:

{org[2]}


👥 Сотрудников:

{members}

"""







# =========================
# Список организаций
# =========================


def list_orgs():



    db = connect()

    cur = db.cursor()



    cur.execute("""

    SELECT id,name,level

    FROM organizations

    LIMIT 20

    """)



    orgs = cur.fetchall()



    db.close()



    if not orgs:


        return """

🏢 Организаций пока нет.

"""



    text = """

🏢 Организации города:


"""



    for org in orgs:


        text += f"""

#{org[0]}

🏢 {org[1]}

⭐ Уровень:
{org[2]}


"""



    return text
