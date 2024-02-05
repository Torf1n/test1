



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