from flask import Flask, request
import vk_api
import os


from database import *
from game import build, city_map
from keyboard import main_keyboard

from jobs import hire_job, city_workers

from admin import (
    admin_menu,
    show_players,
    give_money,
    change_role,
    ban_player,
    unban_player
)

from organizations import (
    create_org,
    join_org,
    organization_info,
    list_orgs
)

from chat import (
    send_chat,
    read_chat
)



app = Flask(__name__)


init_db()



TOKEN = os.getenv(
    "VK_TOKEN"
)


vk = vk_api.VkApi(
    token=TOKEN
).get_api()



CONFIRMATION = "bb6a8d26"




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


    data=request.json



    if data["type"]=="confirmation":

        return CONFIRMATION





    if data["type"]=="message_new":


        msg=data["object"]["message"]


        user_id=msg["from_id"]


        text=msg["text"]


        lower=text.lower()



        create_user(
            user_id
        )


        answer=""



        # =================
        # старт
        # =================


        if lower=="старт":


            create_player(
                user_id
            )


            answer="""

🏙 Добро пожаловать в CellCity!


Твой город создан.


Используй:

город

дом

работы

чат

"""




        # =================
        # город
        # =================


        elif lower=="город":


            player=get_player(
                user_id
            )


            answer=f"""

🏙 Твой город


💰 Деньги:
{player[1]}


👥 Жители:
{player[2]}


😊 Счастье:
{player[3]}


❤️ Здоровье:
{player[4]}


🛡 Безопасность:
{player[5]}


⭐ Репутация:
{player[6]}



{city_map(user_id)}

"""





        # =================
        # строительство
        # =================


        elif lower=="дом":


            answer=build(
                user_id,
                "house"
            )



        elif lower=="завод":


            answer=build(
                user_id,
                "factory"
            )



        elif lower=="парк":


            answer=build(
                user_id,
                "park"
            )






        # =================
        # работы
        # =================


        elif lower=="работы":


            answer=city_workers(
                user_id
            )



        elif lower=="гид":


            answer=hire_job(
                user_id,
                "guide"
            )


        elif lower=="страж":


            answer=hire_job(
                user_id,
                "guard"
            )


        elif lower=="санитар":


            answer=hire_job(
                user_id,
                "medic"
            )


        elif lower=="врач":


            answer=hire_job(
                user_id,
                "doctor"
            )


        elif lower=="радио":


            answer=hire_job(
                user_id,
                "radio"
            )







        # =================
        # Организации
        # =================


        elif lower.startswith(
            "создать организацию "
        ):


            name=text.replace(
                "создать организацию ",
                ""
            )


            answer=create_org(

                user_id,

                name

            )



        elif lower=="организации":


            answer=list_orgs()



        elif lower=="организация":


            answer=organization_info(
                user_id
            )



        elif lower.startswith(
            "вступить "
        ):


            org_id=int(
                lower.replace(
                    "вступить ",
                    ""
                )
            )


            answer=join_org(

                user_id,

                org_id

            )







        # =================
        # Чаты
        # =================


        elif lower=="чат":


            answer=read_chat(

                user_id,

                "global"

            )



        elif lower.startswith(
            "чат "
        ):


            message=text[4:]


            answer=send_chat(

                user_id,

                "global",

                message

            )





        elif lower=="чат орг":


            answer=read_chat(

                user_id,

                "organization"

            )



        elif lower.startswith(
            "чат орг "
        ):


            message=text[8:]


            answer=send_chat(

                user_id,

                "organization",

                message

            )




        elif lower=="чат админ":


            answer=read_chat(

                user_id,

                "admin"

            )



        elif lower.startswith(
            "чат админ "
        ):


            message=text[10:]


            answer=send_chat(

                user_id,

                "admin",

                message

            )







        # =================
        # Админка
        # =================


        elif lower=="админ":


            answer=admin_menu(
                user_id
            )



        elif lower=="игроки":


            answer=show_players(
                user_id
            )



        elif lower.startswith(
            "выдать "
        ):


            data=lower.split()


            answer=give_money(

                user_id,

                int(data[1]),

                int(data[2])

            )



        elif lower.startswith(
            "роль "
        ):


            data=lower.split()


            answer=change_role(

                user_id,

                int(data[1]),

                data[2]

            )



        elif lower.startswith(
            "бан "
        ):


            answer=ban_player(

                user_id,

                int(
                    lower.replace(
                        "бан ",
                        ""
                    )
                )

            )



        elif lower.startswith(
            "разбан "
        ):


            answer=unban_player(

                user_id,

                int(
                    lower.replace(
                        "разбан ",
                        ""
                    )
                )

            )





        else:


            answer="""

Неизвестная команда.


Напишите:

старт

город

чат

админ

"""



        send_message(

            user_id,

            answer

        )



    return "ok"





if __name__=="__main__":


    app.run(

        host="0.0.0.0",

        port=10000

    )
