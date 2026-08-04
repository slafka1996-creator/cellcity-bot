from database import *



BUILDINGS = {

    "house": {

        "name": "🏠 Дом",

        "price": 100,

        "people": 10,

        "money": 0,

        "happiness": 0

    },


    "factory": {

        "name": "🏭 Завод",

        "price": 500,

        "people": 0,

        "money": 100,

        "happiness": -5

    },


    "park": {

        "name": "🌳 Парк",

        "price": 300,

        "people": 0,

        "money": 0,

        "happiness": 10

    }

}




def build(

        user_id,

        building_type

):


    create_player(user_id)


    player = get_player(user_id)


    building = BUILDINGS.get(
        building_type
    )



    if not building:

        return "❌ Такого здания нет"



    money = player[1]

    people = player[2]

    happiness = player[3]

    level = player[4]



    if money < building["price"]:

        return f"""

❌ Недостаточно денег.

Нужно:
💰 {building['price']}

"""



    buildings = get_buildings(
        user_id
    )



    position = find_place(
        buildings
    )



    money -= building["price"]

    people += building["people"]

    happiness += building["happiness"]



    update_player(

        user_id,

        money,

        people,

        happiness,

        level

    )



    add_building(

        user_id,

        position[0],

        position[1],

        building_type

    )



    return f"""

{building['name']} построен!


💰 Деньги: {money}

👥 Жители: {people}

😊 Счастье: {happiness}

"""





def find_place(buildings):


    for y in range(10):

        for x in range(10):

            busy = False


            for b in buildings:

                if b[0]==x and b[1]==y:

                    busy=True


            if not busy:

                return x,y



    return 0,0





def city_map(user_id):


    buildings = get_buildings(
        user_id
    )


    result = []


    for y in range(10):

        line=""


        for x in range(10):

            symbol="⬜"


            for b in buildings:

                if b[0]==x and b[1]==y:


                    if b[2]=="house":

                        symbol="🏠"


                    elif b[2]=="factory":

                        symbol="🏭"


                    elif b[2]=="park":

                        symbol="🌳"



            line+=symbol



        result.append(line)



    return "\n".join(result)
