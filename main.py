from flask import Flask,request
import vk_api

from database import *


app=Flask(__name__)


TOKEN = os.getenv("VK_TOKEN")


vk=vk_api.VkApi(
    token=TOKEN
).get_api()



@app.route("/",methods=["POST"])
def callback():


    data=request.json


    if data["type"]=="confirmation":

        return "СТРОКА_ПОДТВЕРЖДЕНИЯ"



    if data["type"]=="message_new":


        user_id=data["object"]["message"]["from_id"]

        text=data["object"]["message"]["text"].lower()



        if text=="старт":


            create_player(user_id)


            answer="""
🏙 Добро пожаловать в CellCity!

Ваш город создан.

💰 Деньги: 1000
👥 Жители: 0

Команды:

🏠 дом
📊 город
"""


        elif text=="дом":


            answer="""
🏠 Вы построили дом!

+10 жителей
-100 монет
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
