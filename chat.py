from database import *
from database import connect




# ======================
# Получить имя/роль
# ======================


def user_label(user_id):


    user = get_user(
        user_id
    )


    if not user:


        return f"Игрок {user_id}"



    role = user[2]



    if role in [

        "admin",

        "owner",

        "moderator"

    ]:


        return f"🔴 👑 ADMIN {user_id}"



    return f"👤 Игрок {user_id}"







# ======================
# Отправка сообщения
# ======================


def send_chat(

        user_id,

        chat_type,

        message,

        organization_id=0

):


    user = get_user(
        user_id
    )



    if not user:

        create_user(
            user_id
        )



    # админский чат


    if chat_type == "admin":


        if not is_admin(user_id):


            return """

⛔ Доступ только для администрации.

"""



    # чат организации


    if chat_type == "organization":


        user = get_user(
            user_id
        )


        if user[3] == 0:


            return """

❌ Вы не состоите в организации.

"""



        organization_id = user[3]




    add_message(

        user_id,

        chat_type,

        message,

        organization_id

    )



    return """

✅ Сообщение отправлено.

"""







# ======================
# Просмотр чата
# ======================


def read_chat(

        user_id,

        chat_type

):


    organization_id = 0



    user = get_user(
        user_id
    )



    if chat_type == "organization":


        if not user or user[3]==0:


            return """

❌ Вы не состоите в организации.

"""


        organization_id = user[3]





    if chat_type == "admin":


        if not is_admin(user_id):


            return """

⛔ Нет доступа.

"""




    messages = get_messages(

        chat_type,

        organization_id

    )



    if not messages:


        return """

💬 Чат пуст.

"""



    if chat_type=="global":


        title="🌍 Общий чат"


    elif chat_type=="organization":


        title="🏢 Чат организации"


    else:


        title="🔐 Чат администрации"





    result = f"""

{title}


"""



    for msg in reversed(messages):


        user_id = msg[0]

        text = msg[1]


        result += f"""

{user_label(user_id)}

{text}


"""



    return result
