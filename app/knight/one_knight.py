class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list[dict], weapon: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon

    @staticmethod
    def one_knight_create(one_knight_dict: dict):
        for k, v in one_knight_dict.items():
            knight = Knight(
                name=v["name"],
                power=v["power"],
                hp=v["hp"],
                armour=v["armour"],
                weapon=v["weapon"]
            )
            return knight
