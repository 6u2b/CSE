class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon (Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.damage = True
        print("Nice attack")


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.armor_ant
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 42.5)
wiebe_armor = Armor("Armor of the gods.", 100000000000000000000000)

orc = Character("Orc1", 100, sword, Armor("Generic Armor", 2))
orc2 = Character("Wiebe", 100000, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)
