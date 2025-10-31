
class Enemy:
    def __init__(self, name, health, damage, hp_per_round_multiplier, points_on_kill, tags, special_ability, traits, description):
        self.name = name
        self.health = health
        self.damage = damage
        self.hp_per_round_multiplier = hp_per_round_multiplier
        self.points_on_kill = points_on_kill
        self.tags = tags
        self.special_ability = special_ability
        self.traits = traits
        self.description = description

class SpecialEnemy(Enemy):
    def __init__(self, name, health, damage, special_ability, traits=None):
        super().__init__(name, health, damage)
        self.special_ability = special_ability
        self.traits = list(traits) if traits is not None else []
        if special_ability:
            self.traits.append(special_ability)

    def add_trait(self, trait):
        self.traits.append(trait)

    def show_special_traits(self):
        print(f"{self.name}'s traits: {', '.join(self.traits) if self.traits else '(none)'}")

    def enemy_info(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}")

    def enemy_health(self):
        print(f"Current Health: {self.health}")


