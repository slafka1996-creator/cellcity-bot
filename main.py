from flask import Flask, request
import vk_api
import os

from database import *
from game import build, city_map
from keyboard import main_keyboard
from jobs import hire_job, city_workers
from chat import send_chat_message, show_chat


app = Flask(__name__)


init_db()


TOKEN = os.getenv("VK_TOKEN")


vk = vk_api.VkApi(
    token=TOKEN
).get_api()



CONFIRMATION = "ВСТАВЬ_СТРОКУ_ПОДТВЕРЖДЕНИЯ_ВК"





def send_message(
        user_id,
        text
):

    vk.messages.send(

        user_id=user_id,

        message=text,

        keyboard=main_keyboard(),

        random_id=0

    )





@app.route(
    "/",
    methods=["POST"]
)

def callback():


    data = request.json



    if data["type"] == "confirmation":

        return CONFIRMATION




    if data["type"] == "message_new":


        message = data["object"]["message"]


        user_id = message["from_id"]


        text = message["text"].lower()



        create_player(
            user_id
        )



        answer = ""



        # ----------------
        # старт
        # ----------------


        if text == "старт":


            answer = """

🏙 Добро пожаловать в CellCity!


Твой город создан.


💰 Деньги: 1000

👥 Жители: 0

😊 Счастье: 50


Развивай город!

"""



        # ----------------
        # город
        # ----------------


        elif text in [

            "город",

            "🏙 мой город"

        ]:


            city = get_player(
                user_id
            )


            answer = f"""

🏙 Твой город


💰 Деньги:
{city[1]}


👥 Жители:
{city[2]}


😊 Счастье:
{city[3]}


❤️ Здоровье:
{city[4]}


🛡 Безопасность:
{city[5]}


⭐ Репутация:
{city[6]}


Карта:

{city_map(user_id)}

"""





        # ----------------
        # здания
        # ----------------


        elif text in [

            "дом",

            "🏠 дом"

        ]:


            answer = build(

                user_id,

                "house"

            )



        elif text in [

            "завод",

            "🏭 завод"

        ]:


            answer = build(

                user_id,

                "factory"

            )



        elif text in [

            "парк",

            "🌳 парк"

        ]:


            answer = build(

                user_id,

                "park"

            )





        # ----------------
        # профессии
        # ----------------


        elif text == "работы":


            answer = city_workers(
                user_id
            )



        elif text == "гид":


            answer = hire_job(

                user_id,

                "guide"

            )



        elif text == "страж":


            answer = hire_job(

                user_id,

                "guard"

            )



        elif text == "санитар":


            answer = hire_job(

                user_id,

                "medic"

            )



        elif text == "врач":


            answer = hire_job(

                user_id,

                "doctor"

            )



        elif text == "радио":


            answer = hire_job(

                user_id,

                "radio"

            )





        # ----------------
        # чат
        # ----------------


        elif text.startswith("чат "):


            msg = text.replace(

                "чат ",

                ""

            )


            answer = send_chat_message(

                user_id,

                msg

            )




        elif text == "чат":


            answer = show_chat()





        else:


            answer = """

🏙 CellCity команды:


🏙 город


🏠 дом

🏭 завод

🌳 парк


👷 работы


🧭 гид

🛡 страж

🚑 санитар

🩺 врач

📻 радио


💬 чат


"""



        send_message(

            user_id,

            answer

        )



    return "ok"





if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=10000

    )
