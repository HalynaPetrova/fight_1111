from app import knights
from app.knight.one_knight_crate import one_knight_create


def all_knights_create(all_knights_dict: dict):
    knights_list = []
    for i in all_knights_dict.values():
        one_knight = one_knight_create({i["name"]: i})
        knights_list.append(one_knight)
    return knights_list


knights_dict = knights.KNIGHTS

print(all_knights_create(knights_dict)[1].power)