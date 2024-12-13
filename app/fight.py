from app import knights
from app.knight.one_knight import Knight


def battle(knight_1: Knight, knight_2: Knight) -> dict:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
    battle_result_hp = {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp
    }
    return battle_result_hp


#
# first = {
#     "arthur": {
#         "name": "Arthur",
#         "power": 45,
#         "hp": 75,
#         "armour": [
#             {
#                 "part": "helmet",
#                 "protection": 15,
#             },
#             {
#                 "part": "breastplate",
#                 "protection": 20,
#             },
#             {
#                 "part": "boots",
#                 "protection": 10,
#             }
#         ],
#         "weapon": {
#             "name": "Two-handed Sword",
#             "power": 55,
#         },
#         "potion": None,
#     },
#     }
#
# second = {"Red Knight":
#               {"name": "Red Knight",
#         "power": 40,
#         "hp": 70,
#         "armour": [
#             {
#                 "part": "breastplate",
#                 "protection": 25,
#             }
#         ],
#         "weapon": {
#             "name": "Sword",
#             "power": 45
#         },
#         "potion": {
#             "name": "Blessing",
#             "effect": {
#                 "hp": +10,
#                 "power": +5,
#             },
#         },},}
#
# Knight.one_knight_create(first)
# Knight.one_knight_create(second)
# battle(Knight.one_knight_create(first), Knight.one_knight_create(second))
