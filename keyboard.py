import json


def main_keyboard():

    keyboard = {
        "one_time": False,
        "buttons": [

            [
                {
                    "action": {
                        "type": "text",
                        "label": "🏙 Мой город",
                        "payload": "{\"cmd\":\"city\"}"
                    },
                    "color": "primary"
                },

                {
                    "action": {
                        "type": "text",
                        "label": "🏠 Дом",
                        "payload": "{\"cmd\":\"house\"}"
                    },
                    "color": "positive"
                }

            ],


            [

                {
                    "action": {
                        "type": "text",
                        "label": "🏭 Завод",
                        "payload": "{\"cmd\":\"factory\"}"
                    },
                    "color": "negative"
                },


                {
                    "action": {
                        "type": "text",
                        "label": "🌳 Парк",
                        "payload": "{\"cmd\":\"park\"}"
                    },
                    "color": "secondary"
                }

            ]

        ]
    }


    return json.dumps(
        keyboard,
        ensure_ascii=False
    )
