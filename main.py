from flask import Flask,request
import vk_api

from database import *
from flask import Flask, request
import vk_api
import os

from database import *

app=Flask(__name__)
init_db()

TOKEN = os.getenv("VK_TOKEN")


vk=vk_api.VkApi(
    token=TOKEN
).get_api()



@app.route("/",methods=["POST"])
def callback():


    data=request.json


    if data["type"]=="confirmation":

        return "bb6a8d26"



    if data["type"]=="message_new":


        user_id=data["object"]["message"]["from_id"]

        text=data["object"]["message"]["text"].lower()



               if text == "старт":

            create_player(user_id)

            answer = """
🏙 Добро пожаловать в CellCity!

Ваш город создан.

💰 Деньги: 1000
👥 Жители: 0

Команды:

🏠 дом
📊 город
"""


        elif text == "дом":

            player = get_player(user_id)

            if not player:

                create_player(user_id)

                player = get_player(user_id)


            money = player[1]
            people = player[2]
            houses = player[3]


            if money < 100:

                answer = """
❌ Не хватает денег.
"""


            else:

                money -= 100
                people += 10
                houses += 1


                update_player(
                    user_id,
                    money,
                    people,
                    houses
                )


                answer = f"""
🏠 Дом построен!

💰 Деньги: {money}
👥 Жители: {people}
🏠 Дома: {houses}
"""


        elif text == "город":

            player = get_player(user_id)


            if not player:

                create_player(user_id)

                player = get_player(user_id)


            answer = f"""
🏙 Ваш город

💰 Деньги: {player[1]}

👥 Жители: {player[2]}

🏠 Дома: {player[3]}
"""


        else:

            answer = "Напишите: старт"else:

        money -= 100
        people += 10
        houses += 1


        update_player(
            user_id,
            money,
            people,
            houses
        )


        answer = f"""
🏠 Дом построен!

💰 Деньги: {money}
👥 Жители: {people}
🏠 Дома: {houses}
"""
        
        else:

            answer="Напишите: старт"



        vk.messages.send(

            user_id=user_id,

            message=answer,

            random_id=0

        )


    return "ok"



app.run(
host="0.0.0.0",
port=10000
)
