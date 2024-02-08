#
#
#
#
class Superhero:
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def health(self):
        self.health_points *= 2

    def __str__(self):
        return f"heath = {self.health_points} \nnickname = {self.nickname} \nsuperpower = {self.superpower}"

    def __len__(self):
        return len(self.catchphrase)

hero = Superhero(name="Peter Parker", nickname="Spyderman", superpower="Web", health_points=80, catchphrase="With great power comes great responsibility!")

hero.health()
print(hero)
print(len(hero))

class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def apply_superpower(self):
        self.health_points **= 2
        self.fly = True

    def display_superpower_phrase(self):
        return f"{self.fly} in the True_phrase"


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False  # Добавляем новое свойство fly с значением False по умолчанию

    def apply_superpower(self):  # Полиморфизм
        self.health_points **= 2
        self.fly = True

    def display_superpower_phrase(self):  # Полиморфизм
        return f"{self.fly} in the True_phrase"


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False  # Добавляем новое свойство fly с значением False по умолчанию

    def apply_superpower(self):  # Полиморфизм
        self.health_points **= 2
        self.fly = True

    def display_superpower_phrase(self):  # Полиморфизм
        return f"{self.fly} in the True_phrase"


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False  # Добавляем новое свойство fly с значением False по умолчанию

    def apply_superpower(self):  # Полиморфизм
        self.health_points **= 2
        self.fly = True

    def display_superpower_phrase(self):  # Полиморфизм
        return f"{self.fly} in the True_phrase"


class Villain(SpaceHero):  # Наследование от SpaceHero
    people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** self.damage


# Создаем объекты
air_hero = AirHero("Airman", "Airy", "Aerokinesis", 100, "I control the air!", 20)
earth_hero = EarthHero("Earthling", "Terra", "Geokinesis", 120, "I control the earth!", 30)
space_hero = SpaceHero("Spaceman", "Cosmo", "Cosmic Energy Manipulation", 150, "I control the cosmos!", 40)
villain = Villain("Evil", "Villain", "Dark Powers", 200, "I am unstoppable!", 50)

# Применяем методы
air_hero.apply_superpower()
earth_hero.apply_superpower()
space_hero.apply_superpower()
villain.apply_superpower()

print(air_hero.display_superpower_phrase())
print(earth_hero.display_superpower_phrase())
print(space_hero.display_superpower_phrase())
print(villain.display_superpower_phrase())

# Создаем объекты для Villain
villain1 = Villain("Evil1", "Villain1", "Dark Powers", 200, "I am unstoppable!", 50)
villain2 = Villain("Evil2", "Villain2", "Dark Powers", 200, "I am unstoppable!", 60)

# Применяем методы для Villain
villain1.gen_x()
villain2.gen_x()

damage_result = villain1.crit()  # Применяем метод crit для объекта villain1
print(f"Damage result: {damage_result}")