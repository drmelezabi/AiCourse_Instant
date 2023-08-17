## Structural Design Patterns

<a name="Adapter-Method"></a>

### 1. Adapter Method

The Adapter pattern allows incompatible interfaces to work together by providing a wrapper class that converts the interface of one class into another interface.

Example in Python:

```python
class EuropeanSocket:
    def voltage(self):
        return 220

class USASocket:
    def voltage(self):
        return 110

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage() // 2

european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
print(adapter.voltage())  # Output: 110
```

<a name="Bridge-Method"></a>

### 2. Bridge Method

The Bridge pattern separates abstraction from implementation, allowing them to vary independently.

Example in Python:

```python
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1: Drawing a circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2: Drawing a circle at ({x}, {y}) with radius {radius}")

class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self, x, y, radius):
        self.drawing_api.draw_circle(x, y, radius)

class CircleShape(Shape):
    def draw(self, x, y, radius):
        print("Drawing a CircleShape:")
        self.drawing_api.draw_circle(x, y, radius)

shape1 = CircleShape(DrawingAPI1())
shape1.draw(1, 2, 3)  # Output: API1: Drawing a circle at (1, 2) with radius 3
```

<a name="Composite-Method"></a>

### 3. Composite Method

The Composite pattern composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.

Example in Python:

```python
class Graphic:
    def draw(self):
        pass

class Ellipse(Graphic):
    def draw(self):
        print("Drawing an ellipse")

class Circle(Graphic):
    def draw(self):
        print("Drawing a circle")

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def draw(self):
        for graphic in self.graphics:
            graphic.draw()

composite = CompositeGraphic()
composite.add(Circle())
composite.add(Ellipse())
composite.draw()
# Output:
# Drawing a circle
# Drawing an ellipse
```

<a name="Decorator-Method"></a>

### 4. Decorator Method

The Decorator pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

Example in Python:

```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
sugar_milk_coffee = SugarDecorator(milk_coffee)

print(sugar_milk_coffee.cost())  # Output: 8
```

<a name="Facade-Method"></a>

### 5. Facade Method

The Facade pattern provides a simplified interface to a complex system of classes, making it easier to use and understand.

Example in Python:

```python
class SubsystemA:
    def operation_a(self):
        return "Subsystem A operation"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B operation"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        result = []
        result.append(self._subsystem_a.operation_a())
        result.append(self._subsystem_b.operation_b())
        return "\n".join(result)

facade = Facade()
print(facade.operation())
# Output:
# Subsystem A operation
# Subsystem B operation
```

<a name="Proxy-Method"></a>

### 6. Proxy Method

The Proxy pattern provides a surrogate or placeholder for another object to control access to it.

Example in Python:

```python
class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request")

class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        print("Proxy: Logging request")
        self._real_subject.request()

proxy = Proxy()
proxy.request()
# Output:
# Proxy: Logging request
# RealSubject: Handling request
```

<a name="Flyweight-Method"></a>

### 7. Flyweight Method

The Flyweight pattern minimizes memory usage by sharing common parts of objects between multiple objects, instead of duplicating the data.

Example in Python:

```python
class TreeType:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def draw(self, x, y):
        print(f"Drawing a {self._color} tree named {self._name} at ({x}, {y})")

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color):
        if (tree_type := cls._tree_types.get(name)) is None:
            tree_type = TreeType(name, color)
            cls._tree_types[name] = tree_type
        return tree_type

class Tree:
    def __init__(self, x, y, tree_type):
        self._x = x
        self._y = y
        self._tree_type = tree_type

    def draw(self):
        self._tree_type.draw(self._x, self._y)

tree_type1 = TreeFactory.get_tree_type("pine", "green")
tree1 = Tree(1, 2, tree_type1)
tree1.draw()  # Output: Drawing a green tree named pine at (1, 2)
```
