# Завдання 1
# Створіть абстрактний клас Character, атрибути
# name – ім’я
# max_hp – максимальний рівень здоров’я
# hp – нинішній рівень здоров’я
# level – рівень персонажа(від 1 до 20)
# intelligence – стат інтелекту
# strength – стат сили
# dexterity – стат спритності
# mana – стат мани
# defense – стат захисту
# Методи:
# attack() – абстрактний метод
# take_damage(damage) – отримує урон, зменшений на
# захист
# level_up() – збільшує рівень
# increase_stat(stat) – збільшує один з статів на 1
# rest() – відпочинок(відновлює hp до максимального)
# heal(heal_hp) – збільшує hp на heal_hp
import abc


class Character(abc.ABC):
    def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.level = level
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense

    @abc.abstractmethod
    def attack(self):
        raise NotImplementedError("This method should be implemented")

    def take_damage(self, damage):
        damage_level = damage - self.defense
        if damage_level > 0:
            print(f"You took damage.")
            self.hp -= damage_level
            self.hp  = max (0, self.hp)
            print(f"Your current HP: {self.hp}")
        else:
            print(f"You are not damaged")

    def level_up(self):
        self.level += 1
        print("You are leveled up")

    def increase_stat(self, stat):
        if stat == "intelligence":
            self.intelligence += 1
            print(f"You boosted your {stat}")

        elif stat == "strength":
            self.strength += 1
            print(f"You boosted your {stat}")

        elif stat == "dexterity":
            self.dexterity += 1
            print(f"You boosted your {stat}")

        elif stat == "mana":
            self.mana += 1
            print(f"You boosted your {stat}")

        elif stat == "defense":
            self.defense += 1
            print(f"You boosted your {stat}")

        else:
            raise ValueError("Wrong stat")

    def rest(self):
        self.hp = self.max_hp
        print("You use rest")

    def heal(self, heal_hp):
        self.hp += heal_hp

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print("You healed your HP")

# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів: якщо їхній рівень менший за рівень персонажа, то знищує його повністю

# hero1 = Character("John", 100, 80, 3,80, 76, 50, 30, 25)
# hero1.take_damage(10)

class Warrior(Character):
    def attack(self):
        change = 4 * self.strength + 3
        print(f"Нанесено {change} одиниць урону!")
        return change

    def power_strike(self, enemies):
        for enemy in enemies:
            if enemy.level < self.level:
                enemy.hp = 0
                print("Ворога знищено")
            else:
                print("Ворог вижив")


class Enemy(Character):
    def attack(self):
        pass

class Paladin(Character):
    """
    # Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana
    """
    def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
        super().__init__(name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense)
        self.is_protected = False

    def attack(self):
        if self.mana >= 5:
            self.mana -= 5
            return self.strength * 4
        else:
            return self.strength

    #  – збільшує стат defense на 4+level
    def shield(self):
        if not self.is_protected:
            self.defense += 4
            self.defense += self.level
            self.is_protected = True

    #  –  зменшує стат defense на 4+level
    def unshield(self):
        if self.is_protected:
            self.defense -= 4
            self.defense -= self.level
            self.is_protected = False

    # heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana
    def heal_ally(self, ally: Character):
        value = self.level*2 + self.mana*0.2 + 5
        ally.heal(value)

    def rest(self):
        super().rest()

        self.mana += 6

# p1.shield()
# print(p1.hp)
#
# p1.unshield()
# p1.take_damage(60)
# print(p1.hp)
#
# print("Ataka!")
# # print(p2.attack())
# # print(p2.attack())
# # print(p2.attack())
# print(p1.attack())
# print(p1.attack())
# print(p1.attack())
#
# print(p2.attack())
#
# print("Heal_ally")
# print(p2.hp)
# p1.rest()
# p1.heal_ally(p2)
# print(p2.hp)


war1 =  Enemy('Tom',100, 60, 6, 10, 46,30,10,15)
war2 =  Paladin('ТуTom',100, 60, 10, 10, 46,30,10,15)
p1 = Paladin("John", 100, 80, 3,80, 76, 50, 30, 25)
p2 = Paladin("Tom", 100, 70, 2,95, 66, 50, 15, 2)

print(p1.defense)
p1.shield()
print(p1.defense)
p1.shield()
print(p1.defense)
p1.shield()

print()

print(p1.defense)
p1.unshield()
print(p1.defense)
p1.unshield()
print(p1.defense)
p1.unshield()



#
# my_warior = Warrior('Tom',100, 60, 8, 50, 76,50,20,25)
#
# enemies = [war1, war2]
#
# print(war1.hp)
# print(war2.hp)
#
# my_warior.power_strike(enemies)
#
# print(war1.hp)
# print(war2.hp)
#
#
