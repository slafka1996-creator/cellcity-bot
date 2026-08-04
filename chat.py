from database import get_chat, add_chat_message


def send_chat_message(
        user_id,
        message
):

    if len(message) > 200:

        message = message[:200]


    add_chat_message(
        user_id,
        message
    )


    return """

✅ Сообщение отправлено в городской чат.

"""




def show_chat():


    messages = get_chat()


    if not messages:

        return """

🌍 Городской чат пуст.

Будь первым!

"""



    result = """

🌍 Общий чат CellCity


"""



    for msg in reversed(messages):


        user = msg[0]

        text = msg[1]


        result += f"""

👤 Игрок {user}

{text}

"""



    return result
