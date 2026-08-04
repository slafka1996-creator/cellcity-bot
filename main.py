from flask import Flask, request
import vk_api
import os
import json

from database import *
from game import build, city_map
from keyboard import main_keyboard



app = Flask(__name__)


init_db()


TOKEN = os.getenv(
    "VK_TOKEN"
)


vk = vk_api.VkApi(
    token=TOKEN
).get_api()



# Вставь сюда строку,
# которую дал VK Callback API

CONFIRMATION = "bb6a8d26"



def send_message(
        user_id,
        text,
        keyboard=None
):

    params = {

        "user_id": user_id,

        "message": text,

        "random_id": 0

    }


    if keyboard:

        params["keyboard"] = keyboard



    vk.messages.send(
        **params
    )





@app.route(
    "/",
    methods=["POST"]
)

def callback():


    data = request.json



    # подтверждение сервера VK

    if data["type"] == "confirmation":

        return CONFIRMATION





    # новое сообщение

    if data["type"] == "message_new":


        message = data["object"]["message"]


        user_id = message["from_id"]


        text = message["text"].lower()



        create_player(
            user_id
        )



        answer = ""



        # старт

        if text == "старт":


            answer = """

🏙 Добро пожаловать в CellCity!


Твой город создан.


💰 Деньги: 1000

👥 Жители: 0

😊 Счастье: 50


Строй свой город!

"""



        # город

        elif (
            text == "город"
            or
            text == "🏙 мой город"
        ):


            player = get_player(
                user_id
            )


            answer = f"""

🏙 Твой город


💰 Монеты:
{player[1]}


👥 Жители:
{player[2]}


😊 Счастье:
{player[3]}


⭐ Уровень:
{player[4]}


Карта:

{city_map(user_id)}

"""




        # дом

        elif (
            text == "дом"
            or
            text == "🏠 дом"
        ):


            answer = build(
                user_id,
                "house"
            )





        # завод

        elif (
            text == "завод"
            or
            text == "🏭 завод"
        ):


            answer = build(
                user_id,
                "factory"
            )





        # парк

        elif (
            text == "парк"
            or
            text == "🌳 парк"
        ):


            answer = build(
                user_id,
                "park"
            )





        else:


            answer = """

🏙 CellCity


Команды:

🏙 Мой город

🏠 Дом

🏭 Завод

🌳 Парк

"""



        send_message(

            user_id,

            answer,

            main_keyboard()

        )



    return "ok"





if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=10000

    )
