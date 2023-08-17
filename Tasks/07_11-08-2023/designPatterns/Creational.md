## Creational Design Patterns

<a name="Factory-Method"></a>

### 1. Factory Method

The Factory Method pattern provides an interface for creating objects in a super class, but allows subclasses to alter the type of objects that will be created.

Example:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

factory = AnimalFactory()
animal = factory.create_animal("dog")
print(animal.speak())  # Output: Woof!
```

<a name="Abstract-Factory-Method"></a>

### 2. Abstract Factory Method

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

Example:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class DogFactory:
    def create_animal(self):
        return Dog()

class CatFactory:
    def create_animal(self):
        return Cat()

dog_factory = DogFactory()
animal = dog_factory.create_animal()
print(animal.speak())  # Output: Woof!
```

[_Deference between Factory and abstract factory_](https://github.com/drmelezabi/AiCourse_Instant/tree/main/Tasks/07_11-08-2023/designPatterns/deference/FactoryMethod-AbstractFactoryMethod.md)

<a name="Builder-Method"></a>

### 3. Builder Method

The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

Example:

```python
class Pizza:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        return ", ".join(self.toppings)

class PizzaBuilder:
    def create_pizza(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.add_topping("dough")

    def build_sauce(self):
        self.pizza.add_topping("sauce")

    def build_toppings(self):
        self.pizza.add_topping("cheese")

    def get_pizza(self):
        return self.pizza

builder = PizzaBuilder()
builder.create_pizza()
builder.build_dough()
builder.build_sauce()
builder.build_toppings()
pizza = builder.get_pizza()
print(pizza)  # Output: dough, sauce, cheese
```

<a name="Prototype-Method"></a>

### 4. Prototype Method

The Prototype pattern allows creating new instances by copying an existing instance (prototype) instead of creating from scratch.

Example:

```python
class Animal:
    def clone(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow!")

    def clone(self):
        return Cat()

class Dog(Animal):
    def speak(self):
        print("Woof!")

    def clone(self):
        return Dog()

# Create prototype objects
cat_prototype = Cat()
dog_prototype = Dog()

# Copy and use prototypes
animal1 = cat_prototype.clone()
animal2 = dog_prototype.clone()

animal1.speak()  # Output: Meow!
animal2.speak()  # Output: Woof!
```

[_Deference between prototype and create instance_](https://github.com/drmelezabi/AiCourse_Instant/tree/main/Tasks/07_11-08-2023/designPatterns/deference/prototype-instance.md)

<a name="Singleton-Method"></a>

### 5. Singleton Method

The Singleton pattern ensures a class has only one instance and provides a global point of access to that instance.

Example:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
```
