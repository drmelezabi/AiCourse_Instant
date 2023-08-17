**Factory Method:**

Imagine you're building a game where players can choose different characters. Each character has a different ability, like a warrior who can fight and a mage who can cast spells. You use the Factory Method pattern when you have a base class (e.g., `Character`) with subclasses (e.g., `Warrior` and `Mage`). The Factory Method lets each subclass (`WarriorFactory` and `MageFactory`) create its own instances of characters.

Example:

```python
class Character:
    def show_ability(self):
        pass

class Warrior(Character):
    def show_ability(self):
        return "I can fight!"

class Mage(Character):
    def show_ability(self):
        return "I can cast spells!"

class CharacterFactory:
    def create_character(self):
        pass

class WarriorFactory(CharacterFactory):
    def create_character(self):
        return Warrior()

class MageFactory(CharacterFactory):
    def create_character(self):
        return Mage()

# Usage
warrior_factory = WarriorFactory()
mage_factory = MageFactory()

warrior = warrior_factory.create_character()
mage = mage_factory.create_character()

print(warrior.show_ability())  # Output: "I can fight!"
print(mage.show_ability())     # Output: "I can cast spells!"
```

**Abstract Factory Method:**

Now, let's say you want to expand the game and include weapons for each character. Each character type should have its own set of weapons, like a sword for a warrior and a staff for a mage. You can use the Abstract Factory Method pattern to create families of related objects (characters and weapons) that are designed to work together.

Example:

```python
class Weapon:
    def show_power(self):
        pass

class Sword(Weapon):
    def show_power(self):
        return "I can slash with a sword!"

class Staff(Weapon):
    def show_power(self):
        return "I can cast spells with a staff!"

class CharacterWithWeaponFactory:
    def create_character(self):
        pass

    def create_weapon(self):
        pass

class WarriorWithWeaponFactory(CharacterWithWeaponFactory):
    def create_character(self):
        return Warrior()

    def create_weapon(self):
        return Sword()

class MageWithWeaponFactory(CharacterWithWeaponFactory):
    def create_character(self):
        return Mage()

    def create_weapon(self):
        return Staff()

# Usage
warrior_weapon_factory = WarriorWithWeaponFactory()
mage_weapon_factory = MageWithWeaponFactory()

warrior = warrior_weapon_factory.create_character()
warrior_weapon = warrior_weapon_factory.create_weapon()

mage = mage_weapon_factory.create_character()
mage_weapon = mage_weapon_factory.create_weapon()

print(warrior.show_ability())      # Output: "I can fight!"
print(warrior_weapon.show_power()) # Output: "I can slash with a sword!"

print(mage.show_ability())         # Output: "I can cast spells!"
print(mage_weapon.show_power())    # Output: "I can cast spells with a staff!"
```

**Tree Example**

```
Design Patterns
│
├── Factory Method
│   ├── Character
│   │   ├── Warrior
│   │   └── Mage
│   │
│   └── CharacterFactory
│       ├── WarriorFactory
│       └── MageFactory
│
└── Abstract Factory Method
    ├── Character
    │   ├── Warrior
    │   └── Mage
    │
    ├── Weapon
    │   ├── Sword
    │   └── Staff
    │
    └── CharacterWithWeaponFactory
        ├── WarriorWithWeaponFactory
        └── MageWithWeaponFactory
```

In this tree:

- **Factory Method** focuses on creating different types of characters using separate factories for each type.
- **Abstract Factory Method** creates families of related objects, where each family includes both a character and a weapon, and each family has its own factory.

Factory Method deals with one type of product (characters), while Abstract Factory Method deals with multiple related types of products (characters and weapons) that need to work together.
