from flask import Flask, request
import vk_api
import os
import json

from database import *


app = Flask(__name__)


init_db()


TOKEN = os.getenv("VK_TOKEN")


vk = vk_api.VkApi(
    token=TOKEN
).get_api()



CONFIRMATION = "bb6a8d26"



def send(user_id,text):

    vk.messages.send(
        user_id=user_id,
        message=text,
        random_id=0
    )



@app.route("/", methods=["POST"])
def callback():

    data=request.json


    if data["type"]=="confirmation":

        return CONFIRMATION



    if data["type"]=="message_new":


        user_id = data["object"]["message"]["from_id"]

        text = (
            data["object"]
            ["message"]
            ["text"]
            .lower()
        )



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


            create_player(user_id)


            city=get_player(user_id)


            money=city[1]
            people=city[2]
            houses=city[3]



            if money < 100:


                answer="""

❌ Недостаточно денег.

Дом стоит 100 монет.

"""


            else:


                money-=100
                people+=10
                houses+=1


                update_city(
                    user_id,
                    money,
                    people,
                    houses
                )


                answer=f"""

🏠 Новый дом построен!


💰 Деньги: {money}

👥 Жители: {people}

🏠 Дома: {houses}

"""



        elif text=="город":


            create_player(user_id)

            city=get_player(user_id)



            answer=f"""

🏙 Ваш город


💰 Монеты: {city[1]}

👥 Жители: {city[2]}

🏠 Дома: {city[3]}


Карта:

⬜⬜⬜⬜⬜
⬜🏠⬜⬜⬜
⬜⬜⬜⬜⬜

"""



        else:


            answer="""

Команды:

старт
дом
город

"""



        send(
            user_id,
            answer
        )



    return "ok"



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
