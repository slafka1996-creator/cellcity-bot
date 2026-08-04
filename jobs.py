from database import *


JOBS = {

    "guide": {

        "name": "🧭 Гид",

        "price": 200,

        "salary": 20

    },


    "guard": {

        "name": "🛡 Страж",

        "price": 300,

        "salary": 30

    },


    "medic": {

        "name": "🚑 Санитар",

        "price": 250,

        "salary": 25

    },


    "doctor": {

        "name": "🩺 Врач",

        "price": 500,

        "salary": 50

    },


    "radio": {

        "name": "📻 Радиоведущий",

        "price": 400,

        "salary": 40

    }

}





def hire_job(
        user_id,
        job_type
):


    create_player(user_id)


    player = get_player(user_id)


    job = JOBS.get(
        job_type
    )



    if not job:

        return "❌ Такой профессии нет"



    money = player[1]



    if money < job["price"]:


        return f"""

❌ Не хватает денег.

Нужно:
💰 {job['price']}

"""



    jobs = get_jobs(
        user_id
    )


    guides = jobs[1]

    guards = jobs[2]

    medics = jobs[3]

    doctors = jobs[4]

    radio = jobs[5]



    money -= job["price"]



    if job_type == "guide":

        guides += 1


    elif job_type == "guard":

        guards += 1


    elif job_type == "medic":

        medics += 1


    elif job_type == "doctor":

        doctors += 1


    elif job_type == "radio":

        radio += 1





    update_jobs(

        user_id,

        guides,

        guards,

        medics,

        doctors,

        radio

    )



    update_player(

        user_id,

        money,

        player[2],

        player[3],

        player[4],

        player[5],

        player[6],

        player[7]

    )



    return f"""

✅ Новый сотрудник принят!

{job['name']}


💰 Осталось:
{money}

"""







def city_workers(user_id):


    create_player(user_id)


    jobs = get_jobs(
        user_id
    )


    return f"""

👷 Работники города


🧭 Гиды:
{jobs[1]}


🛡 Стражи:
{jobs[2]}


🚑 Санитары:
{jobs[3]}


🩺 Врачи:
{jobs[4]}


📻 Радиоведущие:
{jobs[5]}

"""
